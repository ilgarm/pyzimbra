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

Authentication related methods and classes.

@author: ilgar
"""
from pyzimbra.auth import AuthException, AuthToken, Authenticator
from pyzimbra.soap_auth import SoapAuthenticator
from test.util import load_test_properties


class MockAuthenticator(SoapAuthenticator):
    """
    Mocked authenticator.
    """
    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        SoapAuthenticator.__init__(self)

        load_test_properties(self)

    # ------------------------------------------------------------------ unbound
    def authenticate_admin(self, transport, account_name, password):
        Authenticator.authenticate_admin(self, transport, account_name, password)

        if not account_name == self.admin_account_name:
            raise AuthException('Invalid username')

        if not password == self.admin_password:
            raise AuthException('Invalid password')

        token = AuthToken()
        token.account_name = self.admin_account_name
        token.token = self.token
        token.session_id = self.session_id

        return token


    def auth(self, transport, account_name, password):
        if not account_name == self.account_name:
            raise AuthException('Invalid username')

        if not password == self.password:
            raise AuthException('Invalid password')

        token = AuthToken()
        token.account_name = self.account_name
        token.token = self.token
        token.session_id = self.session_id

        return token


    def pre_auth(self, transport, account_name):
        if not account_name == self.account_name:
            raise AuthException('Invalid username')

        token = AuthToken()
        token.account_name = self.account_name
        token.token = self.token
        token.session_id = self.session_id

        return token
