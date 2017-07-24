#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os.path import join, dirname

from sigfoxapi import __version__, __license__

requirements = [
  r.strip() for r in open(join(dirname(__file__), 'requirements.txt')).readlines()
]

test_requirements = [
  r.strip() for r in open(join(dirname(__file__), 'test_requirements.txt')).readlines()
]

setup(
    name='sigfoxapi',
    version=__version__,
    description='Python wrapper for the Sigfox backend REST API',
    long_description='Terrascript provides a method of generating Terraform files, while harnessing all the features the Python language provides.',
    author='Markus Juenemann',
    author_email='markus@juenemann.net',
    url='https://github.com/mjuenema/python-sigfox-backend-api',
    packages=['sigfoxapi'],
    package_dir={'sigfoxapi': 'sigfoxapi'},
    include_package_data=True,
    install_requires=requirements,
    license=__license__,
    zip_safe=False,
    keywords='sigfox',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
    test_suite='nose.collector',
    tests_require=test_requirements
)