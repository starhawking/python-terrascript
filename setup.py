#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

from os.path import join, dirname

from terrascript import __version__, __license__

# requirements = [
#   r.strip() for r in open(join(dirname(__file__), 'requirements.txt')).readlines()
# ]

test_requirements = [
  r.strip() for r in open(join(dirname(__file__), 'test_requirements.txt')).readlines()
]

setup(
    name='terrascript',
    version=__version__,
    description='Python module for creating Terraform configurations',
    long_description='Terrascript provides a method of generating Terraform files, while harnessing all the features the Python language provides.',
    author='Markus Juenemann',
    author_email='markus@juenemann.net',
    url='https://github.com/mjuenema/python-terrascript',
    packages=find_packages(exclude=['__pycache__']),
    package_dir={'terrascript': 'terrascript'},
    include_package_data=True,
    #install_requires=requirements,
    license=__license__,
    zip_safe=False,
    keywords='terraform',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
    test_suite='nose.collector',
    tests_require=test_requirements
)
