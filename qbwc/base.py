import xmltodict
import requests
import json

from typing import Union, List

from qbwc.generated import types
from qbwc.generated.types import QBXMLMsgsRq, QBXMLMsgsRs
from qbwc.config import uri, request_headers, debug
from qbwc.helpers import (
    dict_to_out, 
    dict_to_in, 
    split_pascal_case
)

_base_xml = '''
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="13.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
    </QBXMLMsgsRq>
</QBXML>
'''.strip()


class QBWCError(Exception):
    pass


def _dicttoxml(d: dict, qbxmlversion: str='13.0'): 
    xml = xmltodict.unparse(d) 
    if qbxmlversion: 
        header, xmldata = xml.split('\n', 1) 
        xml = f'{header}\n<?qbxml version="{qbxmlversion}"?>\n{xmldata}' 
    return xml


def _except_response_has_error(rs: dict) -> None:
    for k, v in rs.items():
        if isinstance(v, dict):
            v = [v]
        for i in v:
            if i['@statusSeverity'] == 'Error':
                e = QBWCError(json.dumps({
                    k: v for k, v in i.items() if k.startswith('@')
                }))
                raise e
    return


def _remove_status_from_rs(rs: dict) -> None:
    for k, v in rs.items():
        if isinstance(v, dict):
            v = [v]
            for i in v:
                for key in tuple(i.keys()):
                    if key.startswith('@'):
                        del i[key]
    return


def request(rq: QBXMLMsgsRq) -> QBXMLMsgsRs:
    rq = dict_to_out(rq)
    base = xmltodict.parse(_base_xml)
    base['QBXML']['QBXMLMsgsRq'].update(rq)
    xml = _dicttoxml(base)
    if debug: print(xml)
    r = requests.post(uri, data=xml, headers=request_headers)
    r.raise_for_status()
    c = r.content
    rs = xmltodict.parse(c)['QBXML']['QBXMLMsgsRs']
    _except_response_has_error(rs)
    _remove_status_from_rs(rs)
    rs = dict_to_in(rs)
    return rs
