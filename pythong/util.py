#!/bin/env python
# -*- coding: utf8 -*-
"""
Contains utility functions used by pythong, including
command parsing.
"""
import os
import yaml
from os.path import join


def ask_yes_no(message, default=None):
    """ Prompt the user for a boolean response.
        Thanks to this useful recipe for help:
            http://code.activestate.com/recipes/577058/
    """
    valid = {'yes': True,
             'y': True,
             'ye': True,
             'no': False,
             'n': False}
    if default:
        prompt = ' [Y/n] '
        valid[''] = True
    else:
        prompt = ' [y/N] '
        valid[''] = False

    while True:
        choice = raw_input(message + prompt).lower()
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
            return str(raw) or default


def determine_directories(name, basedir, snap=False):
    project = dict()

    project['name'] = name
    project['project_dir'] = join(basedir, name)
    project['directories'] = [project['project_dir']]

    if not snap:
        if (not os.path.isdir(join(project['project_dir'], 'bin')) and
                ask_yes_no("Would you like a bin directory?", default=True)):
            project['bin_dir'] = join(project['project_dir'], 'bin')
            project['directories'].append(project['bin_dir'])

        if (not os.path.isdir(join(project['project_dir'], 'tests')) and
                ask_yes_no("Would you like a tests directory?", default=True)):
            project['tests_dir'] = join(project['project_dir'], 'tests')
            project['directories'].append(project['tests_dir'])
    else:
        if not os.path.isdir(join(project['project_dir'], 'bin')):
            project['bin_dir'] = join(project['project_dir'], 'bin')
            project['directories'].append(project['bin_dir'])
        if not os.path.isdir(join(project['project_dir'], 'tests')):
            project['tests_dir'] = join(project['project_dir'], 'tests')
            project['directories'].append(project['tests_dir'])

    project['docs_dir'] = join(project['project_dir'], 'docs')
    project['source_dir'] = join(project['project_dir'], name)

    project['directories'].extend([project['docs_dir'], project['source_dir']])

    return project


def write_config(config_file, data):
    with open(config_file, 'wb') as f:
        yaml.dump(data, f)


def read_config(config_file):
    with open(config_file, 'rb') as f:
        return yaml.safe_load(f)


class Directory(object):
    """
    Thanks to Ralph Bean (http://threebean.org/) for this cd context manager
    (tweaked slightly)
    """

    def __init__(self, new_path):
        self.new_path = new_path

    def __enter__(self, *args, **kwargs):
        self.saved_path = os.getcwd()
        os.chdir(self.new_path)

    def __exit__(self, *args, **kwargs):
        os.chdir(self.saved_path)
