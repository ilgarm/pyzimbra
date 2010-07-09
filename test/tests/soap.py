# -*- coding: utf-8 -*-
"""
################################################################################
# Copyright (c) 2010, Ilgar Mashayev
# 
# E-mail: pyzimbra@lab.az
# Website: http://github.com/ilgarm/pyzimbra
################################################################################
# This file is part of pyzimbra.
# 
# Pyzimbra is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Pyzimbra is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with Pyzimbra.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

@author: ilgar
"""
from pyzimbra import soap
from pyzimbra.soap import SoapException
from test.base import BaseTest
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


    def testNotEmptyHostnamePort(self):
        result = soap.soap_url("localhost:8080")
        self.assertEqual("http://localhost:8080/service/soap", result)


    def testEmptyAdminHostname(self):
        self.assertRaises(SoapException, soap.admin_soap_url, "")


    def testNotEmptyAdminHostname(self):
        result = soap.admin_soap_url("localhost")
        self.assertEqual("https://localhost/service/admin/soap", result)


    def testNotEmptyAdminHostnamePort(self):
        result = soap.admin_soap_url("localhost:8080")
        self.assertEqual("https://localhost:8080/service/admin/soap", result)


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
