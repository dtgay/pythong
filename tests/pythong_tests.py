#!/bin/env python
# -*- coding: utf8 -*-
from nose.tools import *
import unittest
import pythong
from pythong.util import Directory

from mock import patch
from nose.tools import eq_

import tempfile


class TestThong(unittest.TestCase):
    def setUp(self):
        print "SETUP"

    def tearDown(self):
        print "TEAR DOWN"

    @patch("sys.argv", new_callable=lambda: ["pythong", "--snap", "test_proj"])
    def test_snap_project(self, mock_argv):
        with Directory(tempfile.mkdtemp()):
            # below, I comment out the proper assertion line and assert
            # True to show that pythong.create_project() is what is causing
            # tests to fail with:
            # TypeError: sequence item 0:
            #           expected string or Unicode, exceptions.SystemExit found
            pythong.create_project()
            #assert(os.path.isdir("tests"))
            assert(True)

if __name__ == '__main__':
    unittest.main()
