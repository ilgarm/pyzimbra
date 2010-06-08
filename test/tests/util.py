# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from base import BaseTest
from pyzimbra import util
import unittest


class UtilTest(BaseTest, unittest.TestCase):

    # ------------------------------------------------------------------ unbound
    def setUp(self):
        BaseTest.setUp(self)


    def tearDown(self):
        BaseTest.tearDown(self)


    # -------------------------------------------------------------------- tests
    def testEmptyNone(self):
        result = util.empty(None)
        self.assertEqual(True, result)


    def testEmptyString(self):
        result = util.empty("")
        self.assertEqual(True, result)


    def testNotEmptyString(self):
        result = util.empty("some string")
        self.assertEqual(False, result)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
