#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from inoreader.main import *


class Test(unittest.TestCase):

    def test_login(self):
        login()

    def test_list_folders(self):
        list_folders()

    def test_get_subscription_list(self):
        get_subscription_list()

    def test_get_stream_contents(self):
        get_stream_contents('feed/http://www.juzimi.com/feed')


if __name__ == '__main__':
    unittest.main()
