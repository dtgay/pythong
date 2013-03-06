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
