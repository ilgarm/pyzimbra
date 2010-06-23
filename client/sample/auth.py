# -*- coding: utf-8 -*-
"""
Authentication samples.

@author: ilgar
"""
from pyzimbra import soap
from pyzimbra.soap_auth import SoapAuthenticator
from pyzimbra.soap_transport import SoapTransport
from sample.util import load_properties
from pyzimbra.base import ZimbraClientException


def authenticate():
    p = load_properties()

    auth = SoapAuthenticator()
    transport = SoapTransport()

    transport.url = soap.soap_url(p['hostname'])

    auth_token = auth.authenticate(transport, p['account_name'], p['password'])

    print auth_token.token


if __name__ == '__main__':
    try:
        authenticate()
    except ZimbraClientException, e:
        e.print_trace()
