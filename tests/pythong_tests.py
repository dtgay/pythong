#!/bin/env python
# -*- coding: utf8 -*-
from nose.tools import *
import pythong

from mock import patch
from nose.tools import eq_


def setup():
    print "SETUP"


def teardown():
    print "TEAR DOWN"


@patch("sys.argv", new_callable=lambda: ["pythong", "--snap"])
def test_snap_project(self, mock_argv)L
    # TODO: change directory to /tmp/
    pass
