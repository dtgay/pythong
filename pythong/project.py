#!/bin/env python
# -*- coding: utf8 -*-
import os
import jinja2
import readline
from os.path import join
from pythong.util import (ask_yes_no, prompt_input, determine_directories,
                         write_config, read_config)
from pythong.classifiers import CLASSIFIERS

jinja_env = jinja2.Environment(
    loader=jinja2.PackageLoader('pythong', 'templates'))
setup_template = jinja_env.get_template('setup.py.jinja')
distribute_template = jinja_env.get_template('distribute_setup.py.jinja')


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

    project.update(determine_directories(name, os.getcwd(), snap))

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
            classifiers=prompt_classifiers(),
            keywords=prompt_input("Keywords (comma delimited): ").split(','),
            author=prompt_input("Author: "),
            email=prompt_input("Author email: "),
            url=prompt_input("Project URL: "),
            license=prompt_input("License: "),
            requires=prompt_input("Requirements (comma delimited): "
                                  ).split(',')))
    else:
        print "Generating skeletal setup files."

    try:
        write_config(os.path.join(project['project_dir'], '.pythong'), project)
        print "Configuration file written."
    except:
        print "Problem writing config file."

    try:
        write_setup_files(project['project_dir'])
        print "Setup files written."
    except:
        print "Problem writing setup files."


def write_setup_files(project_dir):
    config_data = read_config(os.path.join(project_dir, '.pythong'))
    with open(join(config_data['project_dir'],
                   'distribute_setup.py'), 'w') as f:
        f.write(distribute_template.render(project=config_data))
    with open(config_data['setup_file'], 'w') as f:
        f.write(setup_template.render(project=config_data))


def prompt_classifiers(applicable=None):
    """
    Prompt the user to pick classifiers that apply to their project.
    Optionally takes a list of preselected classifiers (maybe for license later)
    """
    if applicable is None:
        applicable = []
    if not ask_yes_no("Would you like to select classifiers for your project?",
                      default=False):
        return applicable
    while True:
        selection = recurse_prompt(CLASSIFIERS)
        if selection is None:
            return applicable
        applicable.append(selection)
        if len(applicable) > 0:
            print "Selected: \n\t", "\n\t".join(applicable)
        if not ask_yes_no("\nWould you like to add another classifier?",
                          default=True):
            return applicable


def recurse_prompt(tree, sofar=""):
    if tree is None:
        #get rid of the trailing " :: "
        return sofar[:-4]

    if not any(tree.values()):
        return sofar + prompt_optionlist(sorted(tree.keys()))

    selection = prompt_optionlist(sorted(tree.keys()))

    if selection is None:
        return None
    sofar += selection + " :: "
    selection = recurse_prompt(tree[selection], sofar)
    return selection


def prompt_optionlist(options):
    """
    Returns selected option string

    Returns None if user chooses none of the above

    example:
        given: ['MIT', 'GPL', 'LGPL', 'Apache']
        returns: 'GPL'

    """
    for num, opt in zip(range(1, len(options) + 1), options):
        print "[{num}] {opt}".format(num=num, opt=opt)
    print "[0] None"
    selection = raw_input("\nSelect an option from the list above: ")
    while True:
        try:
            if int(selection) not in range(len(options) + 1):
                raise ValueError
            selection = int(selection)
            break
        except ValueError:
            selection = raw_input("Enter a number from the list above: ")
    if selection == 0:
        return None
    return options[selection - 1]
