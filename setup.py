# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='catpandoc',
    version='2020.2.1',
    description='Cat multiple document files to the terminal',
    python_requires='==3.*,>=3.5.0',
    project_urls={
        "documentation":
            "https://github.com/FHPythonUtils/CatPandoc/blob/master/README.md",
        "homepage":
            "https://github.com/FHPythonUtils/CatPandoc",
        "repository":
            "https://github.com/FHPythonUtils/CatPandoc"
    },
    author='FredHappyface',
    classifiers=[
        'Environment :: Console', 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License', 'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Text Processing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    entry_points={"console_scripts": [
        "catpandoc = catpandoc.application:cli"]},
    packages=['CatPandoc'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'art==4.*,>=4.6.0', 'catimage==2020.*,>=2020.5.0',
        'cli2gui==2020.*,>=2020.7.0', 'emoji==0.*,>=0.5.4',
        'pygments==2.*,>=2.6.1', 'pypandoc==1.*,>=1.5.0'
    ],
)
