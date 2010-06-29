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
from base import BaseTest
from mock.auth import MockAuthenticator
from mock.soap import MockTransport
from pyzimbra import zconstant, sconstant
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

        self.assertRaises(AuthException, zclient.invoke, '', '', {}, None)


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

        self.assertRaises(ZimbraClientException, zclient.invoke, '', '', {}, None)


    def testZimbraClientRequest(self):

        zclient = ZimbraClient()
        zclient.transport = MockTransport()
        zclient.authenticate(MockAuthenticator(),
                             self.account_name, self.password)

        params = {}
        res = zclient.invoke(zconstant.NS_ZIMBRA_ACC_URL,
                             sconstant.GetInfoRequest,
                             params)

        self.assertEqual(self.account_name, res.name)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
