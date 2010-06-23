# -*- coding: utf-8 -*-
"""
Soap related mockups.

@author: ilgar
"""
from mock import responses
from pyzimbra.auth import AuthToken
from pyzimbra.base import ZimbraClientTransport
from pyzimbra.soap import SoapException
from util import load_test_properties


class MockTransport(ZimbraClientTransport):
    """
    Mocked transport.
    """
    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        ZimbraClientTransport.__init__(self)

        load_test_properties(self)


    # ------------------------------------------------------------------ unbound
    def invoke(self, req, auth_token):
        
        if auth_token == None:
            auth_token = AuthToken()
            auth_token.account_name = self.account_name
            auth_token.token = self.token
            auth_token.session_id = self.session_id

        return responses.get_response(req, auth_token)


class MockFailingTransport(ZimbraClientTransport):
    """
    Mocked failing transport.
    """
    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        ZimbraClientTransport.__init__(self)

        load_test_properties(self)


    # ------------------------------------------------------------------ unbound
    def invoke(self, req, auth_token):
        raise SoapException('Mocked Error')
