# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='datapack',
    packages=find_packages(),
    version='0.0',
    description='Data packages',
    author='Stéfan van der Walt',
    author_email='stefanv@berkeley.edu',
    url='https://github.com/data-pack/data-pack',
    download_url='https://github.com/data-pack/data-pack/archive/0.0.tar.gz',
    keywords=['data', 'packaging', 'science'],
    classifiers=[],
    requires=["requests"]
)
