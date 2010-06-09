# -*- coding: utf-8 -*-
"""
Account info samples.

@author: ilgar
"""
from ConfigParser import ConfigParser


def load_properties():
    properties = "client-local.properties"
    cfg = ConfigParser()
    cfg.read(properties)

    p = {}
    p['domain'] = cfg.get("domain", "name")
    p['hostname'] = cfg.get("domain", "host")
    p['domain_key'] = cfg.get("domain", "key")

    p['username'] = cfg.get("auth", "username")
    p['account_name'] = '%s@%s' % (p['username'], p['domain'])
    p['password'] = cfg.get("auth", "password")

    return p
