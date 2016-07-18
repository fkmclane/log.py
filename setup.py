#!/usr/bin/env python3
from distutils.core import setup

from log import name, version


setup(
    name=name,
    version=version,
    description='a logger for web applications that use web.py',
    license='MIT',
    author='Foster McLane',
    author_email='fkmclane@gmail.com',
    packages=['log'],
)
