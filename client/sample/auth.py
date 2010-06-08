# -*- coding: utf-8 -*-
"""
Authentication samples.

@author: ilgar
"""
from ConfigParser import ConfigParser
from pyzimbra.soap import SoapAuthenticator, SoapTransport
from pyzimbra import soap


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


def authenticate():
    p = load_properties()

    auth = SoapAuthenticator()
    transport = SoapTransport()

    transport.url = soap.soap_url(p['hostname'])

    auth_token = auth.authenticate(transport, p['account_name'], p['password'])

    print auth_token.token


if __name__ == '__main__':
    authenticate()
