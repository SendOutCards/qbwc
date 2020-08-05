env:
	virtualenv -p python3 env &> /dev/null

dev: env
	./env/bin/pip install -e .
	./env/bin/pip install -r requirements-dev.txt ipython

test: env
	./env/bin/mypy qbwc/

deploy: env test
	./env/bin/python setup.py sdist bdist_wheel upload -r soc

xml: dev
	rm -r data/*.json
	rm -r data/*/*.json
	rm -r data/*/*.xml
	./env/bin/python tasks/qbwc_xml_update.py

types: dev
	rm -r data/*.json
	rm -r data/*/*.json
	./env/bin/python tasks/qbwc_xml_to_json.py
	./env/bin/python tasks/qbwc_xml_to_enum.py
	./env/bin/python tasks/qbwc_xml_to_optional_required_repeatable.py
	./env/bin/python tasks/qbwc_xml_to_types.py