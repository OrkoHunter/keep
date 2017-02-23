#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import sys
from setuptools import setup

if __name__ == "__main__":
    setup(
        name = 'keep',
        version = 0.1,
        author = 'Himanshu Mishra',
        author_email = 'himanshumishra@iitkgp.ac.in',
        description = 'Personal shell command keeper',
        packages = ['keep', 'keep.commands'],
        include_package_data=True,
        install_requires=[
            'click',
            'request',
            'tabulate'
        ],
        entry_points = {
            'console_scripts': [
                'keep = keep.cli:cli'
            ],
        },
    )

