import json
import glob
import xmltodict

xml_files = glob.glob('data/xml/*.xml')

for f in xml_files:
	p = f.rsplit('/', 1)[1].rsplit('.', 1)[0]
	d = xmltodict.parse(open(f).read())
	with open(f'data/json/{p}.json', 'w') as out:
		json.dump(d, out, indent=2)