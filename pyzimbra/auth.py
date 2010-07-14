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
from pyzimbra import util
from pyzimbra.base import ZimbraClientTransport, ZimbraClientException
import abc


class AuthException(ZimbraClientException):
    """
    Authentication exception.
    """
    # -------------------------------------------------------------------- bound
    def __init__(self, message, cause = None):
        ZimbraClientException.__init__(self, message, cause)


class AuthToken(object):
    """
    AuthToken holds current authentication token and sessions id.
    """
    # --------------------------------------------------------------- properties
    account_name = property(lambda self: self._account_name,
                            lambda self, v: setattr(self, '_account_name', v))
    token = property(lambda self: self._token,
                     lambda self, v: setattr(self, '_token', v))
    session_id = property(lambda self: self._session_id,
                          lambda self, v: setattr(self, '_session_id', v))


    # -------------------------------------------------------------------- bound
    def __init__(self):
        self.account_name = None
        self.token = None
        self.session_id = None


    def __str__(self):
        return self.__unicode__()


    def __unicode__(self):
        return ('account_name: %s; token: %s; session_id: %s'
                % (self.account_name, self.token, self.session_id))


class Authenticator(object):
    """
    Authenticator provides methods to authenticate using username/password 
    as a user or administrator or using domain key.
    """
    __metaclass__ = abc.ABCMeta

    # --------------------------------------------------------------- properties
    domains = property(lambda self: self._domains,
                       lambda self, v: setattr(self, '_domains', v))

    # -------------------------------------------------------------------- bound
    def __init__(self):
        self.domains = {}

    # ------------------------------------------------------------------ unbound
    @abc.abstractmethod
    def authenticate_admin(self, transport, account_name, password):
        """
        Authenticates administrator using username and password.
        @param transport: transport to use for method calls
        @param account_name: account name
        @param password: account password
        @return: AuthToken if authentication succeeded
        @raise AuthException: if authentication fails
        """

    @abc.abstractmethod
    def authenticate(self, transport, account_name, password):
        """
        Authenticates account, if no password given tries to pre-authenticate.
        @param transport: transport to use for method calls
        @param account_name: account name
        @param password: account password
        @return: AuthToken if authentication succeeded
        @raise AuthException: if authentication fails
        """
        if not isinstance(transport, ZimbraClientTransport):
            raise ZimbraClientException('Invalid transport')

        if util.empty(account_name):
            raise AuthException('Empty account name')
