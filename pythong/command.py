#!/bin/env python
# -*- coding: utf8 -*-
import os
import re
import shutil


def pin(pin_list):
    """Add a list of files and directories to a MANIFEST.in
        file in the cwd."""
    manifest = open('MANIFEST.in', 'a')
    for pin_item in pin_list:
        if True:
        #if pin_item is a file:
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
