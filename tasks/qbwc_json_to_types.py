import glob
import json

# generate primitive types
types = [
	'from enum import Enum\n'
	'from datetime import datetime, timedelta\n'
	'from decimal import Decimal\n'
	'from typing import Optional, List, Union'
	'\n'
	'from typing_extensions import TypedDict\n'
	'\n'
	'IDTYPE = str\n'
	'STRTYPE = str\n'
	'DATETIMETYPE = datetime\n'
	'DATETYPE = datetime\n'
	'TIMEINTERVALTYPE = timedelta\n'
	'BOOLTYPE = bool\n'
	'GUIDTYPE = str\n'
	'AMTTYPE = Decimal\n'
	'FLOATTYPE = Decimal\n'
	'PRICETYPE = Decimal\n'
	'INTTYPE = int\n'
	'QUANTYPE = int\n'
	'PERCENTTYPE = Decimal'
]

# generate enum types
qb_enum = json.load(open('qbwc/data/enum.json'))
for type_, options in qb_enum.items():
	enum_ = [f'class {type_}(Enum):']
	for option in options:
		option = f'_{option}' if option[0].isnumeric() else option
		option = f'_{option}' if option == 'None' else option
		enum_.append(f'    {option} = "{option}"')
	types.append('\n'.join(enum_))


# generate operation types
endpoint_files = glob.glob('qbwc/data/json/*.json')
endpoint_restr_files = glob.glob('qbwc/data/json_restr/*.json')
types_defined = set()


def assemble_type(name, value, restr, types_):
	if name not in types_defined:
		if isinstance(value, dict):
			type_ = [f'class {name}(TypedDict, total=False):']
			for n, v in value.items():
				if not n.startswith('@'):
					r = restr[n]
					if '#text' in v:
						v = v['#text']
					assemble_type(n, v, r, types_)
					if isinstance(v, dict) or v == 'ENUMTYPE':
						v = n
					if r['@may_repeat']:
						v = f'Union[{v}, List[{v}]]'
					# TODO: This cannot be handled by the type system because:
					#           1. Optional would sill require the key to exist, but
					#              the value type can be None
					#           2. Cannot create a TypedDict with total=True with only the
					#              required params and subclass it with total=False for the optional
					#              because some are params or only required if another isn't present.
					#       Required params need to be handled at runtime. Along with mutually exclusive params.
					# if not r['@required'] or r['@optional']:
					# 	v = f'Optional[{v}]'
					type_.append(f'    {n}: {v}')
			types_.append('\n'.join(type_))
			types_defined.add(name)


msgs_rq_type = ['class QBXMLMsgsRq(TypedDict, total=False):']
msgs_rs_type = ['class QBXMLMsgsRs(TypedDict, total=False):']
for endpoint_file, endpoint_restr_file in zip(endpoint_files, endpoint_restr_files):
	print(endpoint_file, endpoint_restr_file)
	try:
		endpoint = json.load(open(endpoint_file))['QBXML']['QBXMLMsgsRq']
		endpoint_restr = json.load(open(endpoint_restr_file))['QBXMLMsgsRq']
		for name, value in endpoint.items():
			if not name.startswith('@'):
				restr = endpoint_restr[name]
				assemble_type(name, value, restr, types)
			if name.endswith('Rq'):
				msgs_rq_type.append(
					f'    {name}: Optional[Union[{name}, List[{name}]]]'
				)
			if name.endswith('Rs'):
				msgs_rs_type.append(
					f'    {name}: Optional[Union[{name}, List[{name}]]]'
				)
	except KeyError as e:
		print(e)


types.extend((
	'\n'.join(msgs_rq_type),
	'\n'.join(msgs_rs_type)
))


with open('qbwc/generated/types.py', 'w') as out:
	types = '\n\n\n'.join(types)
	out.write(f"{types}\n")