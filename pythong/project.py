#!/bin/env python
# -*- coding: utf8 -*-
import os
import jinja2
import readline
from os.path import join
from pythong.util import ask_yes_no, prompt_input, determine_directories

_here = os.getcwd()

jinja_env = jinja2.Environment(
    loader=jinja2.PackageLoader('pythong', 'templates'))
setup_template = jinja_env.get_template('setup.py.jinja')


def prompt_new_project(name=None, snap=False):
    """
    sampleproject = dict(
        encoding="utf8",
        version="0.0.1",
        shortname="pythong",
        description="This is a description that has words",
        classifiers=["thong", "wearing", "pythonistas"],
        keywords=["more", "thong", "keywords"],
        author="ryansb",
        email="ryansb@csh.rit.edu",
        url="github.com",
        license="MIT",
        requires=["nose", "pyramid"]
    )
    """
    project = dict()

    if not name:
        name = prompt_input("Project name: ")

    if os.path.isdir(name):
        print "A project with that name already exists here."
        exit(1)

    project.update(determine_directories(name, _here, snap))

    # Files
    project['setup_file'] = join(project['project_dir'], "setup.py")
    project['init_file'] = join(project['source_dir'], "__init__.py")
    if project.get('tests_dir'):
        project['test_init_file'] = join(project['tests_dir'], "__init__.py")
        project['test_file'] = join(project['tests_dir'], name + "_tests.py")

    project['files'] = [project['setup_file'], project['init_file']]
    if project.get('tests_dir'):
        project['files'].extend([project['test_init_file'],
                                 project['test_file']])

    # Create project skeleton
    print "Creating structure for new Python project {}.".format(
        project.get("name"))
    for dirname in project.get("directories", []):
        os.mkdir(dirname)
    for f in project.get("files", []):
        project['init_file'] = open(f, 'w').close()

    # Create setup.py file
    # first, set sane defaults
    project.update(dict(
        encoding="utf8",
        version="0.1.0",
        shortname=project.get("name", "horsewithnoname"),
        description="A new project",
        classifiers=[],
        keywords=[],
        author="",
        email="",
        url="",
        license="",
        requires=[]))

    if not snap and ask_yes_no("Would you like help creating a setup.py file?"):
        project.update(dict(
            encoding=prompt_input("Encoding [utf8]: ", default='utf8'),
            version=prompt_input("Version [0.1.0]: ", default='0.1.0'),
            shortname=prompt_input("Short name [%s]: " % project.get("name"),
                                   default=project.get("name")),
            description=prompt_input("Description [A new project]: ",
                                     default='A new project'),
            classifiers=prompt_input("Classifiers (comma delimited): "
                                     ).split(','),
            keywords=prompt_input("Keywords (comma delimited): ").split(','),
            author=prompt_input("Author: "),
            email=prompt_input("Author email: "),
            url=prompt_input("Project URL: "),
            license=prompt_input("License: "),
            requires=prompt_input("Requirements (comma delimited): "
                                  ).split(',')))
    else:
        print "Generating skeletal setup.py file."

    with open(project['setup_file'], 'w') as f:
        f.write(setup_template.render(project=project))
        exit(0)
    exit(1)
