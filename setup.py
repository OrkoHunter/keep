#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import sys
from setuptools import setup

NAME = 'keep'
VERSION = '1.0'

if __name__ == "__main__":
    setup(
            name = NAME,
            version = VERSION,
            author = 'Himanshu Mishra',
            author_email = 'himanshumishra@iitkgp.ac.in',
            description = 'Personal shell command keeper',
            packages = ['keep'],
            entry_points = {
                'console_scripts': [
                    'keep = keep.keep:main'
                    ]
                },
            )

