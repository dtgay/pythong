#!/bin/env python
# -*- coding: utf8 -*-
"""
Contains utility functions used by pythong, including
command parsing.
"""
from os.path import join


def ask_yes_no(message, default=None):
    """ Prompt the user for a boolean response.
        Thanks to this useful recipe for help:
            http://code.activestate.com/recipes/577058/
    """
    valid = {"yes": True,
             "y": True,
             "ye": True,
             "no": False,
             "n": False}
    if default:
        prompt = " [Y/n] "
        valid[''] = True
    else:
        prompt = " [y/N] "
        valid[''] = False

    while True:
        print message + prompt,
        choice = raw_input().lower()
        if choice in valid:
            return valid[choice]
        print "Please respond with 'yes', 'no', 'y', or 'n'."


def prompt_input(prompt, default=None, expected=str):
    """
    If no default is given, the argument is assumed to be required and will
    always return something (no '', no [], etc)

    The "expected" parameter must be a type (str, list, etc) and the prompt
    will do its best to give you back data in that format.
    """
    while True:
        raw = raw_input(prompt)
        if expected is str:
            return str(raw)


def determine_directories(name, basedir, snap=False):
    project = dict()

    project['name'] = name
    project['project_dir'] = join(basedir, name)
    project['directories'] = [project['project_dir']]

    if not snap:
        if ask_yes_no("Would you like a bin directory?", default=True):
            project['bin_dir'] = join(project['project_dir'], "bin")
            project['directories'].append(project['bin_dir'])

        if ask_yes_no("Would you like a tests directory?", default=True):
            project['tests_dir'] = join(project['project_dir'], "tests")
            project['directories'].append(project['tests_dir'])
    else:
        project['bin_dir'] = join(project['project_dir'], "bin")
        project['tests_dir'] = join(project['project_dir'], "tests")
        project['directories'].extend([project['bin_dir'],
                                       project['tests_dir']])

    project['docs_dir'] = join(project['project_dir'], "docs")
    project['source_dir'] = join(project['project_dir'], name)

    project['directories'].extend([project['docs_dir'], project['source_dir']])

    return project
