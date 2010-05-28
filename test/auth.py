# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
import unittest
from pyzimbra import auth
from ConfigParser import ConfigParser


class Test(unittest.TestCase):

    # ------------------------------------------------------------------ unbound
    def setUp(self):
        properties = "test.properties"
        cfg = ConfigParser()
        cfg.read(properties)

        self.domain = cfg.get("domain", "name")
        self.domain_key = cfg.get("domain", "key")

        self.username = "username"
        self.password = "password"

    def tearDown(self):
        pass


    # -------------------------------------------------------------------- tests
    def testAuthEmptyCredentials(self):
        a = auth.Authenticator()
        a.endpoint = "http://%s" % self.domain
        a.domain_key = self.domain_key

        self.assertRaises(auth.AuthException, a.authenticate, "", self.password)
        self.assertRaises(auth.AuthException, a.authenticate, self.username, "")
        self.assertRaises(auth.AuthException, a.authenticate, "", "") 


    def testAuthValidCredentials(self):
        a = auth.Authenticator()
        a.endpoint = "http://%s" % self.domain
        a.domain_key = self.domain_key

        ztoken = a.authenticate(self.username, self.password)

        self.assertTrue(ztoken != None)
        self.assertTrue(len(ztoken.token) > 0)
        self.assertTrue(len(ztoken.session_id) > 0)


    def testAuthInvalidCredentials(self):
        a = auth.Authenticator()
        a.endpoint = "http://%s" % self.domain
        a.domain_key = self.domain_key

        self.assertRaises(auth.AuthException,
                          a.authenticate, self.username, "wrong")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
