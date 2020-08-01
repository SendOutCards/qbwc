import requests
import xmltodict
import bs4
import json
import xmlformatter

xml_format = xmlformatter.Formatter().format_string

INDEX_API_REF_PREFIX = '/app/developer/qbdesktop/docs/api-reference/qbdesktop/'

r = requests.get('https://static.developer.intuit.com/output_html/qbdesktop/index.html')
r = bs4.BeautifulSoup(r.content)
l = [e.get_attribute_list('href')[0] for e in r.find_all(attrs={'class': 'reference internal'})]
p = [i.split(INDEX_API_REF_PREFIX)[1] for i in l if i.startswith(INDEX_API_REF_PREFIX)]


for o in p:
	print(f'starting {o} ...')

	r = requests.get(f'https://static.developer.intuit.com/output_html/qbdesktop/docs/api-reference/qbdesktop/{o}.html')
	r = bs4.BeautifulSoup(r.content)
	c = r.find(attrs={'class': 'code'})
	c = list(list(list(c.children)[0].children)[0])

	xml = []
	comment = None
	for e in c:
		if isinstance(e, bs4.element.NavigableString):
			s = str(e)
		else:
			s = e.text
		xml.append(s)

	xml = ''.join(xml).strip()
	xmltodict.parse(xml)

	with open(f'qbwc/data/xml/{o}.xml', 'wb') as out:
		out.write(xml_format(xml))

	print(f'finished {o}')