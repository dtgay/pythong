#!/bin/env python
# -*- coding: utf8 -*-
import jinja2
import os
from os.path import join
from pythong.util import ask_yes_no, prompt_input
# from jinja2 import Environment, PackageLoader

_here = os.getcwd()

jinja_env = jinja2.Environment(
        loader=jinja2.PackageLoader('pythong', 'templates'))
setup_template = jinja_env.get_template('setup.py.jinja')

# env = Environment(loader=PackageLoader('pythong', 'templates'))
# t = env.get_template('setup.py.jinja')
# print t.render(verbose=True, project=p)


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

    project['name'] = name
    project['project_dir'] = join(_here, name)
    project['directories'] = [project['project_dir']]

    if snap is False:
        if ask_yes_no("Would you like a bin directory?", default=True):
            project['bin_dir'] = join(project['project_dir'], "bin")
            project['directories'].append(project['bin_dir'])

        if ask_yes_no("Would you like a tests directory?", default=True):
            project['tests_dir'] = join(project['project_dir'], "tests")
            project['directories'].append(project['tests_dir'])
    else:
        project['bin_dir'] = join(project['project_dir'], "bin")
        project['directories'].append(project['bin_dir'])
        project['tests_dir'] = join(project['project_dir'], "tests")
        project['directories'].append(project['tests_dir'])

    project['docs_dir'] = join(project['project_dir'], "docs")
    project['source_dir'] = join(project['project_dir'], name)

    project['directories'].extend([project['docs_dir'], project['source_dir']])

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
    if snap is False:
        if ask_yes_no("Would you like help creating a setup.py file?"):
            project.update(dict(
                encoding=prompt_input("Encoding: ",
                                      default='utf-8'),
                version=prompt_input("Version: ",
                                     default='0.1.0'),
                shortname=prompt_input("Short name: ",
                                       default=project.get("name")),
                description=prompt_input("Description: ",
                                         default='A new project'),
                classifiers=prompt_input("Classifiers " \
                                         "(comma delimited): ").split(','),
                keywords=prompt_input("Keywords " \
                                      "(comma delimited): ").split(','),
                author=prompt_input("Author: "),
                email=prompt_input("Author email: "),
                url=prompt_input("Project URL: "),
                license=prompt_input("License: "),
                requires=prompt_input("Requirements " \
                                      "(comma delimited): ").split(',')))
        else:
            print "Generating skeletal setup.py file."
            project.update(dict(
                encoding="utf-8",
                version="0.1.0",
                shortname=project.get("name"),
                description="A new project",
                classifiers=[],
                keywords=[],
                author="",
                email="",
                url="",
                license="",
                requires=[]))
    # TODO: restructure this area to fix the redundancy
    # of having two "generate skeletal setup.py file" code blocks...
    # I want to learn the best way to handle a situation like this
    # in Python.
    else:
        print "Generating skeletal setup.py file."
        project.update(dict(
            encoding="utf-8",
            version="0.1.0",
            shortname=project.get("name"),
            description="A new project",
            classifiers=[],
            keywords=[],
            author="",
            email="",
            url="",
            license="",
            requires=[]))
        f = open(project['setup_file'], 'w')
        f.write(setup_template.render(project=project))
        f.close()
