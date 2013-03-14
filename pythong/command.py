#!/bin/env python
# -*- coding: utf8 -*-
import os
import re
import shutil

from pythong.project import write_setup_files
from pythong.util import ask_yes_no, read_config, write_config


def label(classifiers):
    """Takes a list of classifiers gathered by the
       project.prompt_classifiers() function and adds them to
       the setup.py file."""
    if os.path.isfile('.pythong'):
        try:
            config_data = read_config('.pythong')
            # TODO: fix dict so I can do config_data.project.classifiers,
            # so that I can add cool stuff to the config later that is
            # not about the project? dunno if necessary
            config_data['classifiers'] = classifiers
            write_config('.pythong', config_data)
            print "Modified .pythong config file with new classifiers."
            if ask_yes_no("Do you want to rebuild your setup.py from your new"
                          " config file? All manual changes will be erased.",
                           default=False):
                try:
                    write_setup_files(config_data['project_dir'])
                    print "Setup files written."
                except:
                    print "Problem writing setup files."
        except OSError:
            print "Can't open .pythong file in current directory."
    else:
        print "No .pythong file in current directory."


def pin(pin_list):
    """Add a list of files and directories to a MANIFEST.in
       file in the cwd."""
    # pin_list is a list inside of a list for some reason
    manifest = open('MANIFEST.in', 'a')
    for pin_item in pin_list[0]:
        if os.path.isfile(pin_item):
            manifest.write('include {}\n'.format(pin_item))
        else:
            manifest.write('recursive-include {} *\n'.format(pin_item))
    manifest.close()


def wash():
    """Remove all build/dist/egg-related files and .pyc files"""
    cwd = os.getcwd()
    delete_list = []
    for root, dirnames, filenames in os.walk(cwd):
        files_and_dirs = dirnames + filenames
        delete_list.extend([os.path.join(root, f) for f in files_and_dirs if \
                    re.search(r"\bbuild\b|\bdist\b|[^\s]*\.egg-info|.\.pyc",
                            f)])
    if len(delete_list) < 1:
        print "Your pythong is already sparkly-clean!"
    else:
        for f in delete_list:
            f_path = os.path.join(cwd, f)
            print "deleting {}".format(f_path)
            try:
                os.remove(f_path)
            except OSError:  # this means we've got a directory
                shutil.rmtree(f_path)
        print "Cleaned your pythong of {} files and directories.".format(
                len(delete_list))
