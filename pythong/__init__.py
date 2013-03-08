#!/bin/env python
# -*- coding: utf8 -*-

import argparse
from pythong.project import prompt_new_project


def create_project():
    p = argparse.ArgumentParser()
    p.add_argument('name', help='name of project to be created')
    p.add_argument('--snap', action='store_true',
                    help='quickly create a project skeleton without \
                          any prompting')
    args = p.parse_args()
    prompt_new_project(args.name, args.snap)
