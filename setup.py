#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Flask>=0.11'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='flask_decode',
    version='0.1.0',
    description="Tools for debugging and working with the built-in Flask session cookie",
    long_description=readme + '\n\n' + history,
    author="Kyle Lawlor",
    author_email='klawlor419@gmail.com',
    url='https://github.com/wgwz/flask_decode',
    packages=[
        'flask_decode',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='flask_decode',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
