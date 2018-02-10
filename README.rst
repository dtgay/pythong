pythong
=======

:Author: David Gay <dgay@riseup.net>

Set up a minimal, yet comfortable structure for a Python project.

Features
--------

-   Create a standard Python project directory structure

-   Get help creating your setup.py file, or
    choose to write it yourself by passing the ``--snap``
    command

-   Clear your project of messy build files (build/dist/egg/pyc)
    with the ``--wash`` command

-   Generate a distribute_setup.py file to use a setup.py file
    with distribute

-   Use a tree-style menu to set your PyPI classifiers in your
    setup.py file


Example Usage
-------------

Create a new project like so::

    $ pythong mynewproject

Or, for a quicker setup... ::

    $ pythong --snap

Including the project name in the command is optional.

You can **wash** your pythong of messy build files::

    $ pythong --wash

Pythong will help you add classifiers to your setup.py
during project creation, or after the fact with the **label** command::

    $ pythong --label

Files and directories can be added to the manifest file with **pin**::

    $ pythong --pin [FILE_OR_DIRECTORY]

A full list of options can be seen with::

    $ pythong --help

Get Pythong
-----------

You can install the latest release of Pythong from `PyPI
<https://pypi.python.org/pypi/pythong>`_ with pip::

    $ pip install pythong

You can also get the source from PyPI or `GitHub
<https://github.com/oddshocks/pythong>`_.
Contributions are welcome! Yay, software freedom!

License
-------

pythong is released under the GNU GPLv3+.

Contributors
------------

Feel free to add your name.

-   David Gay  <oddshocks@riseup.net>
-   Ryan Scott Brown  <ryansb@csh.rit.edu>
-   Ralph Bean  <rbean@redhat.com>
