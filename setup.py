#!/bin/env python
# -*- coding: utf8 -*-
from setuptools import setup, find_packages

try:
    import multiprocessing, logging
except ImportError:
    pass


"""This manual version import is needed for setup.py
if we want to have the version pulled from one location
because if we import python.version to get it, the install
will fail because jinja2 will be missing."""
__version__ = "" # this will be pulled from version.py
with open('pythong/version.py') as f:
    exec(f)


setup(name='pythong',
      version=__version__,
      description="Set up a minimal, yet comfortable structure \
                    for a Python project",
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python :: 2",
          "Topic :: Software Development",
          "Topic :: Utilities",
      ],
      keywords='python development project bootstrap',
      author='David Gay',
      author_email='oddshocks@riseup.net',
      url='http://github.com/oddshocks/pythong',
      license='GPLv3+',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      test_suite='nose.collector',
      tests_require=['nose', 'mock'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['jinja2', 'pyyaml'],
      entry_points="""
      [console_scripts]
      pythong = pythong:parse_command
      """
)
