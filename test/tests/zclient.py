# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from base import BaseTest
from lxml import etree
from mock.auth import MockAuthenticator
from mock.soap import MockTransport
from pyzimbra import zconstant
from pyzimbra.auth import AuthException
from pyzimbra.base import ZimbraClientException
from pyzimbra.zclient import ZimbraClient
import unittest


class ZimbraClientTest(BaseTest, unittest.TestCase):

    # ------------------------------------------------------------------ unbound
    def setUp(self):
        BaseTest.setUp(self)


    def tearDown(self):
        BaseTest.tearDown(self)


    # -------------------------------------------------------------------- tests
    def testZimbraClientNoTransport(self):

        zclient = ZimbraClient()

        self.assertRaises(ZimbraClientException, zclient.authenticate,
                          MockAuthenticator(), self.account_name, self.password)


    def testZimbraClientNoAuth(self):

        zclient = ZimbraClient()

        self.assertRaises(AuthException, zclient.invoke, None)


    def testZimbraClientAuth(self):

        zclient = ZimbraClient()
        zclient.transport = MockTransport()

        zclient.authenticate(MockAuthenticator(),
                             self.account_name, self.password)


    def testZimbraClientWrongAuth(self):

        zclient = ZimbraClient()
        zclient.transport = MockTransport()

        self.assertRaises(AuthException, zclient.authenticate,
                          MockAuthenticator(), self.account_name, 'wrong')


    def testZimbraClientNoRequest(self):

        zclient = ZimbraClient()
        zclient.transport = MockTransport()
        zclient.authenticate(MockAuthenticator(),
                             self.account_name, self.password)

        self.assertRaises(ZimbraClientException, zclient.invoke, None)


    def _testZimbraClientRequest(self):

        zclient = ZimbraClient()
        zclient.hostname = self.hostname
        zclient.authenticate(self.account_name, self.password)

        req = etree.Element('test', nsmap=zconstant.NS_ZIMBRA_ACC_MAP)
        res = zclient.invoke(req)


    def _testZimbraClientRequestAlternativeToken(self):

        zclient = ZimbraClient()
        zclient.hostname = self.hostname
        zclient.authenticate(self.account_name, self.password)

        req = etree.Element('test', nsmap=zconstant.NS_ZIMBRA_ACC_MAP)
        zclient.invoke(req, self.alt_auth_token)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
