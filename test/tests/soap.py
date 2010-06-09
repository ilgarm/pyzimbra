# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from base import BaseTest
from pyzimbra import soap
from pyzimbra.soap import SoapException
import unittest


class SoapTest(BaseTest, unittest.TestCase):

    # ------------------------------------------------------------------ unbound
    def setUp(self):
        BaseTest.setUp(self)


    def tearDown(self):
        BaseTest.tearDown(self)


    # -------------------------------------------------------------------- tests
    def testEmptyHostname(self):
        self.assertRaises(SoapException, soap.soap_url, "")


    def testNotEmptyHostname(self):
        result = soap.soap_url("localhost")
        self.assertEqual("http://localhost/service/soap", result)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
