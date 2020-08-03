import json
import glob
import xmltodict

ENUM_SUBSTR = ' may have one of the following values: '

xml_files = glob.glob('data/xml/*.xml')

enum = {}
enum_default = {}
enum_private = {}
for f in xml_files:
	lines = open(f).readlines()
	for line in lines:
		line = line.strip()
		if line.startswith('<!--') and ENUM_SUBSTR in line:
			line = line[5:-4]
			type_, options = line.split(ENUM_SUBSTR)
			ops = []
			for option in options.split(', '):
				option = option.strip()
				if option:
					if ' ' in option:
						option, extra = option.split(' ')
						if extra.lower() == '[default]':
							enum_default[type_] = option
						elif extra.lower() == '[private]':
							enum_private[type_] = option
						else:
							raise Exception(f'Unknown extra for {option}: {extra}')
					ops.append(option)
			enum[type_] = ops

with open('data/enum.json', 'w') as out:
	json.dump(enum, out, indent=2)

with open('data/enum_default.json', 'w') as out:
	json.dump(enum_default, out, indent=2)

with open('data/enum_private.json', 'w') as out:
	json.dump(enum_private, out, indent=2)