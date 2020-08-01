import json

from typing import Tuple, Union, Any, List, Optional, Set, Callable, Iterator
from collections import OrderedDict
from string import ascii_uppercase
from datetime import datetime
from fnmatch import fnmatch
from decimal import Decimal

from dateutil.parser import parse as iso_parse
from toolz import curry, complement, compose

import xmltodict
import requests


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


def _to_number(s: str) -> Union[str, int, Decimal]:
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


def to_pascal_case(s: str) -> str:
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


def _is_upper(c: str) -> bool:
    return c in ascii_uppercase


_is_not_upper = complement(_is_upper)


def infer_types(d: Any) -> Any:
    is_str = isinstance(d, str)
    if is_str and _is_iso(d):
        return iso_parse(d)
    elif is_str:
        return _maybe_convert_s(d)
    else:
        return d


def serialize_types_for_xml(d: Any) -> Any:
    if isinstance(d, datetime):
        return d.strftime('%Y-%m-%dT%H:%M:%S')
    elif isinstance(d, bool):
        return 'true' if d else 'false'
    elif isinstance(d, (int, float, Decimal)):
        return str(d)
    else:
        return d


def split_pascal_case(s: str) -> Iterator[str]:
    p = 0
    l = ''
    n = ''
    sl = len(s) - 1
    for i, c in enumerate(s):
        if i != sl:
            n = s[i+1]
        if (
            c in ascii_uppercase and 
            (l not in ascii_uppercase or n not in ascii_uppercase) and 
            i != 0
        ):
            yield s[p:i]
            p = i
        l = c
    yield s[p:]


def to_snake_case(s: str) -> str:
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
def dict_keys_to(fn: Callable, out: bool, d: Any, converter: Optional[Callable]=None) -> Any:
    if isinstance(d, (dict, OrderedDict)):
        # intentionally converting to dict if originally OrderedDict
        return {
            fn(k): dict_keys_to(fn, out, v)
            for k, v in d.items()
        }
    elif isinstance(d, (list, tuple, set)):
        return d.__class__(map(dict_keys_to(fn, out), d))
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


@curry
def dict_converter(fn: Callable, d: Any) -> Any:
    if isinstance(d, (dict, OrderedDict)):
        # intentionally converting to dict if originally OrderedDict
        return {
            fn(k): dict_converter(fn, v)
            for k, v in d.items()
        }
    elif isinstance(d, (list, tuple, set)):
        return d.__class__(map(dict_converter(fn), d))
    else:
        return fn(d)


dict_to_out = dict_converter(serialize_types_for_xml)
dict_to_in = dict_converter(infer_types)

dict_keys_to_pascal_case = dict_keys_to(to_pascal_case)
dict_keys_to_pascal_case_out = dict_keys_to_pascal_case(converter=serialize_types_for_xml)
dict_keys_to_snake_case = dict_keys_to(to_snake_case)
dict_keys_to_snake_case_out = dict_keys_to_snake_case(converter=infer_types)
