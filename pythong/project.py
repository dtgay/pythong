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
        self.project_dir = join(_here, name)
        self.bin_dir = join(self.project_dir, "bin")
        self.docs_dir = join(self.project_dir, "docs")
        self.source_dir = join(self.project_dir, name)
        self.tests_dir = join(self.project_dir, "tests")

        # Create structure
        print "Creating structure for new Python project " + \
                self.name
        # Create directories
        bash_command = "mkdir {0} {1} {2} {3} {4}".format(
                self.project_dir, self.bin_dir, self.docs_dir,
                self.source_dir, self.tests_dir)
        subprocess.Popen(bash_command, shell=True)
