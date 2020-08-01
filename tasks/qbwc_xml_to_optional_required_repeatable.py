import json
import glob
import xmltodict

OPTIONAL = 'optional'
REQUIRED = 'required'
REPEATABLE = 'may repeat'
OPTIONS = {OPTIONAL, REQUIRED, REPEATABLE}

xml_files = glob.glob('qbwc/data/xml/*.xml')


def add_restrictions(nesting, r, options):
	if nesting:
		key = nesting[0]
		if key not in r:
			r[key] = {}
		if len(nesting) == 1:
			r[key].update({
				f'@{option.replace(" ", "_")}': option in options
				for option in OPTIONS
			})
		else:
			add_restrictions(nesting[1:], r[nesting[0]], options)


for f in xml_files:
	lines = open(f).readlines()
	restrictions = {}
	nesting = []
	for i in range(1, len(lines) - 1):
		line = lines[i]
		ws = 0
		for c in line:
			if c == ' ':
				ws += 1
			else:
				break
		line = line.strip()
		if line.startswith('<!--'):
			line = line[5:-4].strip()
			if any(o in line for o in OPTIONS):
				options = line.split(', ')
				if not all(o in OPTIONS for o in options):
					raise Exception(f'unexpected options: {nesting} {options}')
				else:
					add_restrictions(nesting, restrictions, options)
		ns = len(nesting)*2
		if ns >= ws and nesting:
			nesting.pop()
		if line[:2] not in ('</', '<!'):
			split_c = ' ' if ' ' in line else '>'
			node = line[1:].split(split_c)[0]
			nesting.append(node)
	p = f.rsplit('/', 1)[1].rsplit('.', 1)[0]
	with open(f'qbwc/data/json_restr/{p}.json', 'w') as out:
		json.dump(restrictions, out, indent=2)

