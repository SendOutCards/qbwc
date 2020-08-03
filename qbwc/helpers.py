from typing import Union, Any, List, Optional, Callable, Iterator
from collections import OrderedDict
from string import ascii_uppercase
from datetime import datetime
from fnmatch import fnmatch
from decimal import Decimal

from dateutil.parser import parse as iso_parse
from toolz import curry, compose


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
