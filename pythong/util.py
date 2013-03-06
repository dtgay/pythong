"""
Contains utility functions used by pythong, including
command parsing.
"""

from pythong.project import Project

import argparse


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("name")
    args = p.parse_args()
    new_project = Project(args.name)


def ask_yes_no(message, default="yes"):
    """ Prompt the user for a boolean response.
        Thanks to this useful recipe for help:
            http://code.activestate.com/recipes/577058/
    """
    valid = {"yes": True,
             "y": True,
             "ye": True,
             "no": False,
             "n": False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("Invalid default answer: {}".format(default))

    while True:
        print message + prompt
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print "Please respond with 'yes' or 'no' \
                    (or 'y' or 'n')."


def generate_setup_file():
    pass # mmm, pass
