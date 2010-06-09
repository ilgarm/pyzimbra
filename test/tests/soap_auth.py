# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from base import BaseTest
from mock.soap import MockFailingTransport, MockTransport
from pyzimbra.auth import AuthException
from pyzimbra.soap_auth import SoapAuthenticator
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
