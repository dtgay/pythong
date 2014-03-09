CHANGELOG
=========

A bit late, but I am starting a changelog. Feel free to go back
in commit history and add details of previous updates.
-- message written at version 0.6.4 release

# 0.7.1

*   `.pythong` file now contains the data it used to prior to 0.7.
    The removal of this caused more problems than it solved,
    at least for now.

# 0.7

*   The `.pythong` config file now only contains information related
    to file locations and directories, not `setup.py`-type data.

*   New projects now come with an empty manifest file

*   Clarify a message or two

*   Remove some accidental `q` logging traces and an unused import

# 0.6.6

*   Fix import issue related to how the program version number was
    being set.

# 0.6.5

*   Program and setup.py load version number from the __init__ file
    in call cases.

# 0.6.4

*   setup.py is no longer moved to setup.py.old if setup.py is empty.
