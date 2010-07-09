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

Zimbra client related methods and classes.

@author: ilgar
"""
from pyzimbra import util
from pyzimbra.auth import AuthException
from pyzimbra.base import ZimbraClientException


class ZimbraClient(object):
    """
    Zimbra client main class.
    """
    # --------------------------------------------------------------- properties
    auth_token = property(lambda self: self._auth_token,
                          None)
    transport = property(lambda self: self._transport,
                         lambda self, v: setattr(self, '_transport', v))

    # -------------------------------------------------------------------- bound
    def __init__(self):
        self._auth_token = None
        self.transport = None

    # ------------------------------------------------------------------ unbound
    def authenticate_admin(self, authenticator, account_name, password):
        """
        Authenticates zimbra administrative account.
        @param authenticator: authenticator to use
        @param account_name: account email address
        @param password: account password
        @raise AuthException: if authentication fails
        @raise SoapException: if soap communication fails
        """
        if self.transport == None:
            raise ZimbraClientException('Invalid transport')

        self._auth_token = authenticator.authenticate_admin(self.transport,
                                                            account_name,
                                                            password)

    def authenticate(self, authenticator, account_name, password):
        """
        Authenticates zimbra account.
        @param authenticator: authenticator to use
        @param account_name: account email address
        @param password: account password
        @raise AuthException: if authentication fails
        @raise SoapException: if soap communication fails
        """
        if self.transport == None:
            raise ZimbraClientException('Invalid transport')

        self._auth_token = authenticator.authenticate(self.transport,
                                                      account_name, password)


    def invoke(self, ns, request_name, params, auth_token=None):
        """
        Invokes zimbra method using established authentication session.
        @param req: zimbra request
        @param auth_token: alternative authentication session,
          if not provided existing one will be used 
        @return: zimbra response
        @raise AuthException: if authentication fails
        @raise SoapException: wrapped server exception
        """
        if self.auth_token == None and auth_token == None:
            raise AuthException('Unable to invoke zimbra method')

        if util.empty(request_name):
            raise ZimbraClientException('Invalid request')

        token = auth_token if auth_token != None else self._auth_token
        return self.transport.invoke(ns, request_name, params, token)
