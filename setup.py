#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description': 'Time-off budgeter and tracker.',
    'author': 'Michael Jezierny',
    'url': 'https://github.com/alsophian/pterotrack',
    'author_email': 'michael@alsophian.net',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pterotrack'],
    'scripts': [],
    'name': 'Pterotrack'
}

setup(**config)
