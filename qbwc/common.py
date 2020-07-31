import json

from typing import Tuple, Union, Any, List, Optional, Set, Callable
from collections import OrderedDict
from string import ascii_uppercase
from datetime import datetime
from fnmatch import fnmatch
from decimal import Decimal

from dateutil.parser import parse as iso_parse
from toolz import curry, complement, compose

import xmltodict
import requests

from qbwc.config import uri, request_headers, debug

_base_xml = '''
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="13.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
    </QBXMLMsgsRq>
</QBXML>
'''.strip()

_iso_pattern_datetime = '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]'
_iso_pattern_date = '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
_str_false = {'false', 'False'}
_str_true = {'true', 'True'}


def _is_iso(s: Any) -> bool:
    return (
        isinstance(s, str) and 
        (fnmatch(s[:19], _iso_pattern_datetime) or 
         fnmatch(s[:10], _iso_pattern_date))
    )


def _to_boolean(s: str) -> Union[str, bool]:
    if s in _str_false:
        return False
    elif s in _str_true:
        return True
    else:
        return s


def _to_number(s: str) -> Union[str, Decimal]:
    if s.isnumeric():
        return int(s)
    elif s.count('.') == 1 and all(i.isnumeric() for i in s.split('.')):
        return Decimal(s)
    else:
        return s


_maybe_convert_s = compose(_to_boolean, _to_number)


class MutuallyExclusiveParamsError(Exception):
    pass


class QBWCError(Exception):
    pass


def _to_pascal_case(s: str) -> str:
    parts = s.split('_')
    return ''.join(f'{p[0].upper()}{p[1:]}' for p in parts)


def _is_not_trailing_c(s: str, i: int) -> bool:
    return _has_preceding_c(s, i) and _has_following_c(s, i)


def _has_preceding_c(s: str, i: int) -> bool:
    return i != 0


def _has_following_c(s: str, i: int) -> bool:
    return i != len(s) - 1


def _is_preceding_upper(s: str, i: int) -> bool:
    return _has_preceding_c(s, i) and _is_upper(s[i-1])


def _is_following_upper(s: str, i: int) -> bool:
    return _has_following_c(s, i) and _is_upper(s[i+1])


def _doesnt_have_trailing_(s: str, i: int) -> bool:
    return s[i-1] != '_' and s[i+1] != '_'


def _is_upper(c):
    return c in ascii_uppercase


_is_not_upper = complement(_is_upper)


def _to_snake_case(s: str) -> str:
    n = []
    for i, c in enumerate(s):
        if _is_upper(c):
            if (
                _is_not_trailing_c(s, i) and 
                _doesnt_have_trailing_(s, i) and
                not _is_preceding_upper(s, i)
            ):
                n.append('_')
            if not any((_is_preceding_upper(s, i), _is_following_upper(s, i))):
                c = c.lower()
        n.append(c)
    return ''.join(n)


# NOTE: Also converts python types to strings or strings to python types, depending on whether the
#       dict is going to be serialized (out) or not.
@curry
def _dict_keys_to(fn, out: bool, d: Any) -> Any:
    if isinstance(d, (dict, OrderedDict)):
        # intentionally converting to dict if originally OrderedDict
        return {
            fn(k): _dict_keys_to(fn, out, v)
            for k, v in d.items()
        }
    elif isinstance(d, (list, tuple, set)):
        return d.__class__(map(_dict_keys_to(fn, out), d))
    elif out and isinstance(d, datetime):
        return d.strftime('%Y-%m-%dT%H:%M:%S')
    elif out and isinstance(d, bool):
        return 'true' if d else 'false'
    elif not out and _is_iso(d):
        return iso_parse(d)
    elif not out and isinstance(d, str):
        return _maybe_convert_s(d)
    else:
        return d


_dict_keys_to_pascal_case = _dict_keys_to(_to_pascal_case, True)
_dict_keys_to_snake_case = _dict_keys_to(_to_snake_case, False)


def _dicttoxml(d: dict, qbxmlversion: str='13.0'): 
    xml = xmltodict.unparse(d) 
    if qbxmlversion: 
        header, xmldata = xml.split('\n', 1) 
        xml = f'{header}\n<?qbxml version="{qbxmlversion}"?>\n{xmldata}' 
    return xml


def _operation_to_package_keys(operation: str) -> Tuple[str, str, str]:
    operation_resource, _ = operation.rsplit('_', 1)
    return tuple(map(_to_pascal_case, (
        f'{operation}_rq',
        f'{operation}_rs',
    ))) + (f'{operation_resource}_ret',)


def _dict_exclude_if_None(data: Union[dict, list]) -> dict:
    if isinstance(data, dict):
        data = [data]
    data = [{k: v for k, v in d.items() if v is not None} for d in data]
    if len(data) == 1:
        return data[0]
    else:
        return data


# TODO: Handle cases where params nested in param values can contain mutually exclusive options
#       EXAMPLE: txn_date_range_filter.date_macro and txn_date_range_filter.[from|to]_txn_date
def except_on_mutually_exclusive_params(mutually_exclusive_params: List[set], kwargs: dict) -> None:
    param_keys = set(_dict_exclude_if_None(kwargs).keys())
    for mep in mutually_exclusive_params:
        mep = param_keys & mep
        if len(mep) > 1:
            raise MutuallyExclusiveParamsError(f'{mep}')


def except_without_required_params( 
    required: Set[str],
    # purpose of this field is to prevent updates that don't specify changes or queries
    # that are too broad
    minimum_additional_fields: int,
    args_or_kwargs: Union[List[dict], dict]
) -> None:
    minimum_fields = minimum_additional_fields + len(required)
    args = [args_or_kwargs] if isinstance(args_or_kwargs, dict) else args_or_kwargs
    for arg in args:
        arg_keys = set(_dict_exclude_if_None(arg))
        # if all of right not in left
        missing = required - arg_keys
        if missing:
            e = QBWCError(f'Call missing required fields: {missing}')
            raise e
        count_over_minimum = len(arg_keys) - minimum_fields
        if count_over_minimum < 0:
            e = QBWCError(f'Must include {-count_over_minimum} additional field(s) to query, mod, or add resource.')
            raise e


def _except_response_has_error(rss: Union[dict, List[dict]], ret: str) -> None:
    if isinstance(rss, dict):
        rss = [rss]
    for rs in rss:
        if rs['@status_severity'] == 'Error':
            e = QBWCError(json.dumps({
                k: v for k, v in rs.items() if k != ret 
            }))
            e.data = rs
            raise e


def request(operation: str, data: Union[dict, List[dict]]) -> List[OrderedDict]:
    data = _dict_exclude_if_None(data)
    rq, rs, ret = _operation_to_package_keys(operation)
    d = _dict_keys_to_pascal_case({rq: data})
    base = xmltodict.parse(_base_xml)
    base['QBXML']['QBXMLMsgsRq'].update(d)
    xml = _dicttoxml(base)
    debug and print(xml)
    r = requests.post(uri, data=xml, headers=request_headers)
    r.raise_for_status()
    c = r.content
    debug and print(c[:1000])
    r = _dict_keys_to_snake_case(xmltodict.parse(c)['QBXML']['QBXMLMsgsRs'][rs])
    _except_response_has_error(r, ret)
    return  [i[ret] for i in r] if isinstance(r, list) else r[ret]
