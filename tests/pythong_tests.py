#!/bin/env python
# -*- coding: utf8 -*-
from nose.tools import *
import unittest
import pythong
from pythong.util import Directory

from mock import patch
from nose.tools import eq_

import tempfile


def fake_prompt_optionlist(input_list):
    def fr(_):
        return input_list.pop(0)
    return fr


class TestThong(unittest.TestCase):

    def setUp(self):
        print "SETUP"

    def tearDown(self):
        print "TEAR DOWN"

    @patch("pythong.project.prompt_optionlist",
           new=fake_prompt_optionlist(["Development Status",
                                       None,
                                       "Operating System",
                                       "POSIX",
                                       "Linux"]
                                      )
           )

    def test_optionlist(self):
        from pythong.classifiers import CLASSIFIERS
        from pythong.project import recurse_prompt
        assert(recurse_prompt(CLASSIFIERS) is None)
        assert(recurse_prompt(CLASSIFIERS) == "Operating System :: POSIX :: Linux")

if __name__ == '__main__':
    unittest.main()
