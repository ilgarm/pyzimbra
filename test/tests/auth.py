# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from base import BaseTest
from mock.auth import MockAuthenticator
from mock.soap import MockTransport
from pyzimbra import util
from pyzimbra.auth import AuthToken, AuthException
from pyzimbra.base import ZimbraClientException
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

        self.assertEquals(None, auth_token.token)
        self.assertEquals(None, auth_token.session_id)


    def testAuthTokenNotEmpty(self):
        auth_token = AuthToken()
        auth_token.token = 'token'
        auth_token.session_id = 'sessionid'

        self.assertFalse(util.empty(auth_token.token))
        self.assertFalse(util.empty(auth_token.session_id))


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
        self.assertEquals(self.token, auth_token.token)
        self.assertEquals(self.session_id, auth_token.session_id)


    def testAuthInvalidCredentials(self):
        a = MockAuthenticator()
        transport = MockTransport()

        self.assertRaises(AuthException,
                          a.authenticate, transport, "wrong", self.password)
        self.assertRaises(AuthException,
                          a.authenticate, transport, self.account_name, "wrong")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
