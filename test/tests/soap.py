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


    def testEmptyProxyHostname(self):
        self.assertRaises(SoapException, soap.proxy_url, "")


    def testNotEmptyProxyHostname(self):
        result = soap.proxy_url("localhost")
        self.assertEqual('http://localhost', result)
        
        result = soap.proxy_url("localhost", "", "")
        self.assertEqual('http://localhost', result)
        
        result = soap.proxy_url("localhost", "user", "pass")
        self.assertEqual('http://user:pass@localhost', result)
        
        result = soap.proxy_url("localhost", "user", "pass", 8080)
        self.assertEqual('http://user:pass@localhost:8080', result)
        
        result = soap.proxy_url("localhost", "user", "pass", 80)
        self.assertEqual('http://user:pass@localhost', result)
        
        result = soap.proxy_url("localhost", port=80)
        self.assertEqual('http://localhost', result)
        
        result = soap.proxy_url("localhost", port=8080)
        self.assertEqual('http://localhost:8080', result)
        
        result = soap.proxy_url("localhost", port=8080, scheme='http')
        self.assertEqual('http://localhost:8080', result)
        
        result = soap.proxy_url("localhost", port=3128, scheme='https')
        self.assertEqual('https://localhost:3128', result)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
