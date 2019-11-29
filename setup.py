#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
import re
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Flask>=0.11"]

test_requirements = ["pytest"]

setup_requirements = ["pytest-runner"]

setup(
    name="flask_cookie_decode",
    version=find_version("flask_cookie_decode", "__init__.py"),
    description="Tools for debugging and working with the built-in Flask session cookie",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    author="Kyle Lawlor",
    author_email="klawlor419@gmail.com",
    url="https://github.com/wgwz/flask-cookie-decode",
    packages=find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["fcd = flask_cookie_decode.__main__:main"]},
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords="flask_cookie_decode",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    tests_require=test_requirements,
    extras_require={"test": test_requirements},
    setup_requires=setup_requirements,
)
