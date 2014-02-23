#!/bin/python
# -*- coding: utf-8 -*-
"""
@author: Deryck Arnold
"""

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pylifx",
    version = "0.0.1",
    author = "Deryck Arnold",
    author_email = "derkarnold@gmail.com",
    description = ("A Python library to control and monitor LIFX bulbs"),
    license = "Creative Commons Attribution 3.0 Unported License",
    keywords = "lifx smart light bulb",
    url = "https://pypi.python.org/pypi/pylifx",
    packages = ['pylifx'],
    long_description = read('README.txt'),
	package_data={'': ['LICENSE.txt']},
	install_requires = ['bitstring>=3.1.2', 'netifaces>=0.7'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Attribution Assurance License",
    ],
)