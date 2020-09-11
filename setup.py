#!/usr/bin/env python

from setuptools import setup, find_packages

from os.path import join, dirname

from terrascript import __version__, __license__

# requirements = [
#   r.strip() for r in open(join(dirname(__file__), 'requirements.txt')).readlines()
# ]

test_requirements = [
    r.strip()
    for r in open(join(dirname(__file__), "test_requirements.txt")).readlines()
]

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="terrascript",
    version=__version__,
    description="Python module for creating Terraform configurations",
    long_description=long_description,
    author="Markus Juenemann",
    author_email="markus@juenemann.net",
    url="https://github.com/mjuenema/python-terrascript",
    packages=find_packages(exclude=["__pycache__"]),
    package_dir={"terrascript": "terrascript"},
    include_package_data=True,
    # install_requires=requirements,
    license=__license__,
    zip_safe=False,
    keywords="terraform",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    test_suite="nose.collector",
    tests_require=test_requirements,
)
