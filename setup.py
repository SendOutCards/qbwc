from setuptools import setup, find_packages

setup(
	name='qbwc',
	version='0.1.0',
	description='QuickBooks Web Connector SDK',
	author='Tyler Lovely',
	author_email='tyler.n.lovely@gmail.com',
	packages=find_packages(),
	install_requires=open('requirements.txt').readlines()
)