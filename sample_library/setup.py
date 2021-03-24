"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sample_library',
    version='0.0.1',
    description='A Python package for adding two numbers together with Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bassboink/package_demo',
    author='Mitchell Wendt',
    author_email='mitchell.wendt@huntington.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.7',
    install_requires=['numpy'],
)