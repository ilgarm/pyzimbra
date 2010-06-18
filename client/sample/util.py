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

    p['proxy_scheme'] = cfg.get("proxy", "scheme")
    p['proxy_hostname'] = cfg.get("proxy", "host")
    p['proxy_port'] = cfg.get("proxy", "port")
    p['proxy_username'] = cfg.get("proxy", "username")
    p['proxy_password'] = cfg.get("proxy", "password")

    p['username'] = cfg.get("auth", "username")
    p['account_name'] = '%s@%s' % (p['username'], p['domain'])
    p['password'] = cfg.get("auth", "password")

    return p
