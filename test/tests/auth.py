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
from pyzimbra import util
from pyzimbra.auth import AuthToken, AuthException
from pyzimbra.base import ZimbraClientException
from test.base import BaseTest
from test.mock.auth import MockAuthenticator
from test.mock.soap import MockTransport
import unittest


class AuthTest(BaseTest, unittest.TestCase):

    # ------------------------------------------------------------------ unbound
    def setUp(self):
        BaseTest.setUp(self)


    def tearDown(self):
        BaseTest.tearDown(self)


    # -------------------------------------------------------------------- tests
    def testAuthTokenEmpty(self):
        auth_token = AuthToken()

        self.assertEquals(None, auth_token.account_name)
        self.assertEquals(None, auth_token.token)
        self.assertEquals(None, auth_token.session_id)


    def testAuthTokenNotEmpty(self):
        auth_token = AuthToken()
        auth_token.account_name = 'account'
        auth_token.token = 'token'
        auth_token.session_id = 'sessionid'

        self.assertFalse(util.empty(auth_token.account_name))
        self.assertFalse(util.empty(auth_token.token))
        self.assertFalse(util.empty(auth_token.session_id))


    def testAdminAuthEmptyTransport(self):
        a = MockAuthenticator()

        self.assertRaises(ZimbraClientException, a.authenticate_admin, None, "", "")


    def testAdminAuthEmptyCredentials(self):
        a = MockAuthenticator()
        transport = MockTransport()

        self.assertRaises(AuthException,
                          a.authenticate_admin, transport, "", self.password)
        self.assertRaises(AuthException,
                          a.authenticate_admin, transport, self.username, "")
        self.assertRaises(AuthException,
                          a.authenticate_admin, transport, "", "")


    def testAdminAuthValidCredentials(self):
        a = MockAuthenticator()
        transport = MockTransport()

        auth_token = a.authenticate(transport, self.account_name, self.password)

        self.assertTrue(auth_token != None)
        self.assertEquals(self.account_name, auth_token.account_name)
        self.assertEquals(self.token, auth_token.token)
        self.assertEquals(self.session_id, auth_token.session_id)


    def testAdminAuthInvalidCredentials(self):
        a = MockAuthenticator()
        transport = MockTransport()

        self.assertRaises(AuthException,
                          a.authenticate, transport, "wrong", self.password)
        self.assertRaises(AuthException,
                          a.authenticate, transport, self.account_name, "wrong")


    def testAuthEmptyTransport(self):
        a = MockAuthenticator()

        self.assertRaises(ZimbraClientException, a.authenticate, None, "", "")


    def testAuthEmptyCredentials(self):
        a = MockAuthenticator()
        transport = MockTransport()

        self.assertRaises(AuthException,
                          a.authenticate, transport, "", self.password)
        self.assertRaises(AuthException,
                          a.authenticate, transport, self.username, "")
        self.assertRaises(AuthException,
                          a.authenticate, transport, "", "")


    def testAuthValidCredentials(self):
        a = MockAuthenticator()
        transport = MockTransport()

        auth_token = a.authenticate(transport, self.account_name, self.password)

        self.assertTrue(auth_token != None)
        self.assertEquals(self.account_name, auth_token.account_name)
        self.assertEquals(self.token, auth_token.token)
        self.assertEquals(self.session_id, auth_token.session_id)


    def testAuthInvalidCredentials(self):
        a = MockAuthenticator()
        transport = MockTransport()

        self.assertRaises(AuthException,
                          a.authenticate, transport, "wrong", self.password)
        self.assertRaises(AuthException,
                          a.authenticate, transport, self.account_name, "wrong")


    def testPreAuthEmptyCredentials(self):
        a = MockAuthenticator()
        transport = MockTransport()

        self.assertRaises(AuthException,
                          a.authenticate, transport, "")


    def testPreAuthValidCredentials(self):
        a = MockAuthenticator()
        transport = MockTransport()

        auth_token = a.authenticate(transport, self.account_name)

        self.assertTrue(auth_token != None)
        self.assertEquals(self.account_name, auth_token.account_name)
        self.assertEquals(self.token, auth_token.token)
        self.assertEquals(self.session_id, auth_token.session_id)


    def testPreAuthInvalidCredentials(self):
        a = MockAuthenticator()
        transport = MockTransport()

        self.assertRaises(AuthException,
                          a.authenticate, transport, "wrong", self.password)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
