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

Soap related methods and classes.

@author: ilgar
"""
from pyzimbra import zconstant, sconstant
from pyzimbra.auth import AuthException, AuthToken, Authenticator
from pyzimbra.soap import SoapException


class SoapAuthenticator(Authenticator):
    """
    Soap authenticator.
    """
    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        Authenticator.__init__(self)

    # ------------------------------------------------------------------ unbound
    def authenticate(self, transport, account_name, password):
        """
        Authenticates account using soap method.
        """
        Authenticator.authenticate(self, transport, account_name, password)

        params = {sconstant.E_ACCOUNT: account_name,
                  sconstant.E_PASSWORD: password}
        try:
            res = transport.invoke(zconstant.NS_ZIMBRA_ACC_URL,
                                   sconstant.AuthRequest,
                                   params,
                                   None)
        except SoapException as exc:
            raise AuthException(unicode(exc), exc)

        auth_token = AuthToken()
        auth_token.account_name = account_name
        auth_token.token = res.authToken
        auth_token.session_id = res.sessionId

        return auth_token
