#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Flask>=0.11'
]

test_requirements = [
    'pytest'
]

setup_requirements = [
    'pytest-runner'
]

setup(
    name='flask_cookie_decode',
    version='0.3.0',
    description="Tools for debugging and working with the built-in Flask session cookie",
    long_description=readme + '\n\n' + history,
    author="Kyle Lawlor",
    author_email='klawlor419@gmail.com',
    url='https://github.com/wgwz/flask-cookie-decode',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='flask_cookie_decode',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    tests_require=test_requirements,
    setup_requires=setup_requirements
)
