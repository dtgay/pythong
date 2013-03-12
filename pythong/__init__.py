#!/bin/env python
# -*- coding: utf8 -*-

import argparse
from pythong.command import wash
from pythong.project import prompt_new_project


def parse_command():
    p = argparse.ArgumentParser()
    p.add_argument('name', nargs='?', default='',
                   help='name of project to be created')
    # TODO: have version be pulled from setup.py variable?
    p.add_argument('--version', action='version',
                   version='you are using version 0.0.1 of the pythong')
    p.add_argument('-s, --snap', action='store_true',
                   help='quickly create a project skeleton without \
                          any prompting')
    p.add_argument('-w, --wash', action='store_true',
                   help='clean your pythong of messy build/dist/egg files')
    args = p.parse_args()
    if args.wash:
        pythong.wash()
    else:
        prompt_new_project(args.name, args.snap)
