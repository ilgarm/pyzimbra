# -*- coding: utf-8 -*-
"""
Authentication related methods and classes.

@author: ilgar
"""
from pyzimbra.auth import Authenticator, AuthException, AuthToken
from util import load_test_properties


class MockAuthenticator(Authenticator):
    """
    Mocked authenticator.
    """
    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        Authenticator.__init__(self)

        load_test_properties(self)

    # ------------------------------------------------------------------ unbound
    def authenticate(self, transport, account_name, password):
        Authenticator.authenticate(self, transport, account_name, password)

        if not account_name == self.account_name:
            raise AuthException('Invalid username')

        if not password == self.password:
            raise AuthException('Invalid username')

        token = AuthToken()
        token.token = self.token
        token.session_id = self.session_id

        return token
