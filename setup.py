from setuptools import setup, find_packages

setup(
    name='qbwc',
    version='0.2.1',
    description='QuickBooks Web Connector SDK',
    author='Tyler Lovely',
    author_email='tyler.n.lovely@gmail.com',
    packages=find_packages(),
    url="https://pypi.hq.sendoutcards.com/pypi/qbwc",
    install_requires=open('requirements.txt').readlines(),
    python_requires='>=3.6'
)
