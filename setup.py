#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os.path as op


from codecs import open
from setuptools import setup


def read(fname):
    ''' Return the file content. '''
    here = op.abspath(op.dirname(__file__))
    with open(op.join(here, fname), 'r', 'utf-8') as fd:
        return fd.read()

readme = read('README.rst')
changelog = read('CHANGES.rst').replace('.. :changelog:', '')

requirements = [
    "requests",
    "xmltodict",
    "lxml",
    "furl",
]

version = ''
version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                    read(op.join('shiba', '__init__.py')),
                    re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')


setup(
    name='Shiba',
    author="Maxime Boguta",
    author_email="maxime.boguta@epitech.eu",
    version=version,
    url='https://github.com/ShibaAPI/shiba',
    packages=["shiba"],
    install_requires=requirements,
    zip_safe=True,
    description="A Python API for PriceMinister WebServices",
    long_description=readme + '\n\n' + changelog,
    keywords=["api", "priceminister", "python", "webservices"],
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
