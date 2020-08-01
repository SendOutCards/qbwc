# NOTE: WIP

from typing import List

from qbwc.generated import types
from qbwc.generated.types import QBXMLMsgsRq, QBXMLMsgsRs
from qbwc.helpers import split_pascal_case


pkg = {'Rq', 'Rs', 'Ret'}
ops = {'Query', 'Mod', 'Add', 'Del'}
_resources = {}
_base_xml = '''
<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="13.0"?>
<QBXML>
    <QBXMLMsgsRq onError="stopOnError">
    </QBXMLMsgsRq>
</QBXML>
'''.strip()


def populate_resource(t: str, s: List[str], _resources: dict) -> str:
	type_ getattr(types, t)
	if type_ not in (QBXMLMsgsRq, QBXMLMsgsRs):
		p = s[-1]
		o = s[-2]
		# print(o)
		# assert o in ops
		r = ''.join(s[:-2] if o in ops else s[:-1])
		if r not in _resources:
			_resources[r] = {}
		if p == 'Ret':
			_resources[r][p] = type_
		else:
			if o not in _resources[r]:
				_resources[r][o] = {}
			_resources[r][o][p] = type_


for t in dir(types):
	s = tuple(split_pascal_case(t))
	if s[-1] in pkg:
		populate_resource(t, s, _resources)


print(_resources)