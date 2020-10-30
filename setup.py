#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os
import sys
from setuptools import setup

from keep import about

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

if __name__ == "__main__":
    setup(
        name=about.__name__,
        packages=['keep', 'keep.commands'],
        version=about.__version__,
        description='Personal shell command keeper',
        long_description=long_description,
        author='Himanshu Mishra',
        author_email='himanshu.mishra.kgp@gmail.com',
        url="https://github.com/orkohunter/keep",
        download_url="https://github.com/orkohunter/keep/archive/master.zip",
        include_package_data=True,
        install_requires=[
            'click',
            'requests',
            'terminaltables',
            'PyGithub'
        ],
        entry_points={
            'console_scripts': [
                'keep=keep.cli:cli'
            ],
        },
    )
