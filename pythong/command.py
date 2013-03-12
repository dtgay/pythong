#!/bin/env python
# -*- coding: utf8 -*-
import os
import re


def wash():
    """Remove all build/dist/egg-related files"""
    cwd = os.getcwd()
    for f in os.listdir(cwd):
        if re.search('build|dist|*egg-info', f):
            os.remove(os.path.join(cwd, f))
