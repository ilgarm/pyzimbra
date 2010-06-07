# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from ConfigParser import ConfigParser
from pyzimbra import auth
import unittest


class AuthTest(unittest.TestCase):

    # ------------------------------------------------------------------ unbound
    def setUp(self):
        properties = "test.properties"
        cfg = ConfigParser()
        cfg.read(properties)

        self.domain = cfg.get("domain", "name")
        self.hostname = cfg.get("domain", "host")
        self.domain_key = cfg.get("domain", "key")

        self.username = cfg.get("auth", "username")
        self.password = cfg.get("auth", "password")

    def tearDown(self):
        pass


    # -------------------------------------------------------------------- tests
    def testAuthEmptyCredentials(self):
        a = auth.Authenticator()
        a.hostname = self.hostname
        a.domain = self.domain
        a.domain_key = self.domain_key

        self.assertRaises(auth.AuthException, a.authenticate, "", self.password)
        self.assertRaises(auth.AuthException, a.authenticate, self.username, "")
        self.assertRaises(auth.AuthException, a.authenticate, "", "") 


    def testAuthValidCredentials(self):
        a = auth.Authenticator()
        a.hostname = self.hostname
        a.domain = self.domain
        a.domain_key = self.domain_key

        ztoken = a.authenticate(self.username, self.password)

        self.assertTrue(ztoken != None)
        self.assertTrue(len(ztoken.token) > 0)
        self.assertTrue(len(ztoken.session_id) > 0)


    def testAuthInvalidCredentials(self):
        a = auth.Authenticator()
        a.hostname = self.hostname
        a.domain = self.domain
        a.domain_key = self.domain_key

        self.assertRaises(auth.AuthException,
                          a.authenticate, self.username, "wrong")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
