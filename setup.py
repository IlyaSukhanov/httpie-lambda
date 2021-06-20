#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="httpie-lambda",
    version="0.1",
    description="AWS Lambda invoke transport plugin for HTTPie",
    long_description=open("README.rst").read().strip(),
    author="Ilya Sukhanov",
    author_email="ilya@sukhanov.net",
    url="https://github.com/IlyaSukhanov/httpie-lambda",
    install_requires=[
        "lambda-requests>=1.1",
        "httpie>=2.4.0",
    ],
    entry_points={
        "httpie.plugins.transport.v1": [
            "httpie_lambda = httpie_lambda:LambdaTransportPlugin"
        ]
    },
    extras_require={
        "testing": [
            "pip~=20.3",
            "flake8",
            "tox",
            "coverage",
            "pytest",
            "pyflakes",
            "pytest-cov",
            "bandit",
            "black~=21.5b1",
            "isort",
            "wheel",
            "twine",
        ],
    },
    license="MIT license",
    zip_safe=False,
    keywords="HTTPie",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
