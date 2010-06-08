# -*- coding: utf-8 -*-
"""
Test related methods and classes.

@author: ilgar
"""
from ConfigParser import ConfigParser


def load_test_properties(test):
    cfg = ConfigParser()
    if len(cfg.read("test.properties")) == 0:
        cfg.read("../test.properties")

    test.domain = cfg.get("domain", "name")
    test.hostname = cfg.get("domain", "host")
    test.domain_key = cfg.get("domain", "key")

    test.username = cfg.get("auth", "username")
    test.account_name = '%s@%s' % (test.username, test.domain)
    test.password = cfg.get("auth", "password")
    test.token = cfg.get("auth", "token")
    test.session_id = cfg.get("auth", "session_id")
