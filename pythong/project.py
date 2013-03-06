#!/bin/env python
# -*- coding: utf8 -*-
import os
from os.path import join
import pythong.util

_here = os.getcwd()


class Project(object):
    """
    A Python project.
    """

    def __init__(self, name):
        self.name = name

        # Directories
        self.project_dir = join(_here, name)
        self.bin_dir = join(self.project_dir, "bin")
        self.docs_dir = join(self.project_dir, "docs")
        self.source_dir = join(self.project_dir, name)
        self.tests_dir = join(self.project_dir, "tests")

        self.directories = [self.project_dir, self.bin_dir, self.docs_dir,
                            self.source_dir, self.tests_dir]

        # Files
        self.setup_file = join(self.project_dir, "setup.py")
        self.init_file = join(self.source_dir, "__init__.py")
        self.test_init_file = join(self.tests_dir, "__init__.py")
        self.test_file = join(self.tests_dir, self.name + "_tests.py")

        self.files = [self.setup_file, self.init_file, self.test_init_file,
                      self.test_file]

        # Create project skeleton
        print "Creating structure for new Python project {}.".format(
            self.name)
        for dirname in self.directories:
            os.mkdir(dirname)
        for f in self.files:
            self.init_file = open(f, 'w').close()

        # Create setup.py file
        wants_help = pythong.util.ask_yes_no(
            "Would you like help creating a setup.py file?")
        if wants_help:
            print "I will help!"
        else:
            print "Generating skeletal setup.py file."
            #f = open(self.setup_file, 'w').write("try:\n
