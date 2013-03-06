import os
from os.path import join
import subprocess

_here = os.getcwd()


class Project(object):
    """
    A Python project.
    """

    def __init__(self, name):
        self.name = name
        bash_command = "mkdir " + join(_here, name)
        print "running command: " + bash_command
        subprocess.Popen(bash_command, shell=True)
