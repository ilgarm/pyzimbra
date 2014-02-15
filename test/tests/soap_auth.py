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
from pyzimbra.auth import AuthException
from pyzimbra.soap_auth import SoapAuthenticator
from test.base import BaseTest
from test.mock.soap import MockFailingTransport, MockTransport
import unittest


class SoapAuthTest(BaseTest, unittest.TestCase):

    # ------------------------------------------------------------------ unbound
    def setUp(self):
        BaseTest.setUp(self)


    def tearDown(self):
        BaseTest.tearDown(self)


    # -------------------------------------------------------------------- tests
    def testWorkingTransport(self):
        a = SoapAuthenticator()
        transport = MockTransport()

        auth_token = a.authenticate(transport, self.account_name, self.password)

        self.assertTrue(auth_token != None)
        self.assertEquals(self.token, auth_token.token)
        self.assertEquals(self.session_id, auth_token.session_id)


    def testFailingTransport(self):
        a = SoapAuthenticator()
        transport = MockFailingTransport()

        self.assertRaises(AuthException,
                          a.authenticate, transport, self.account_name, self.password)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
