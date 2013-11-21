#!/bin/env python
# -*- coding: utf8 -*-
from setuptools import setup, find_packages

try:
    import multiprocessing, logging
except ImportError:
    pass

import pythong

setup(name='pythong',
      version=pythong.__version__,
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
