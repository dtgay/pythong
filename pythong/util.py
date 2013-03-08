#!/bin/env python
# -*- coding: utf8 -*-
"""
Contains utility functions used by pythong, including
command parsing.
"""


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
    If no default is given, the argumend is assumed to be required and will
    always return something (no '', no [], etc)

    The "expected" parameter must be a type (str, list, etc) and the prompt
    will do its best to give you back data in that format.
    """
    while True:
        raw = raw_input(prompt)
        if default is None:
            return None

        if expected is str:
            return str(raw)
