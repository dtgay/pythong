#!/bin/env python
# -*- coding: utf8 -*-

import argparse
from pythong.project import prompt_new_project


def create_project():
    p = argparse.ArgumentParser()
    p.add_argument("name")
    args = p.parse_args()
    prompt_new_project(args.name)
