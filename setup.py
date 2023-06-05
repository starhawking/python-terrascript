from setuptools import setup, find_packages
from pathlib import Path

version_file = Path(__file__).resolve().parent / "terrascript" / "__version__.py"
with version_file.open() as f:
    exec(f.read())

setup(
    name="terrascript",
    version=__version__,
    description="Python module for creating Terraform configurations",
    long_description=Path("README.rst").read_text(),
    author="Markus Juenemann",
    author_email="markus@juenemann.net",
    url="https://github.com/mjuenema/python-terrascript",
    packages=find_packages(exclude=["__pycache__"]),
    include_package_data=True,
    license="BSD License",
    zip_safe=False,
    keywords="terraform",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    test_suite="nose.collector",
    tests_require=[
        r.strip() for r in Path("test_requirements.txt").read_text().splitlines()
    ],
)
