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
from pyzimbra.soap_auth import SoapAuthenticator
from pyzimbra.soap_transport import SoapTransport
import abc


class ZimbraSoapClient(object):
    """
    Zimbra client main class.
    """
    __metaclass__ = abc.ABCMeta

    # --------------------------------------------------------------- properties
    transport = property(lambda self: self._transport,
                         lambda self, v: setattr(self, '_transport', v))
    authenticator = property(lambda self: self._authenticator,
                             lambda self, v: setattr(self, '_authenticator', v))
    auth_token = property(lambda self: self._auth_token,
                          lambda self, v: setattr(self, '_auth_token', v))


    # -------------------------------------------------------------------- bound
    def __init__(self, soap_url, domains={}, proxy_url=None):
        self.transport = SoapTransport()
        self.transport.soap_url = soap_url
        
        if proxy_url != None:
            self.transport.proxy_url = proxy_url

        self.authenticator = SoapAuthenticator()
        self.authenticator.domains = domains
        
        self.auth_token = None


    # ------------------------------------------------------------------ unbound
    def invoke(self, ns, request_name, params={}, simplify=False):
        """
        Invokes zimbra method using established authentication session.
        @param req: zimbra request
        @parm params: request params
        @param simplify: True to return python object, False to return xml struct
        @return: zimbra response
        @raise AuthException: if authentication fails
        @raise SoapException: wrapped server exception
        """
        if self.auth_token == None:
            raise AuthException('Unable to invoke zimbra method')

        if util.empty(request_name):
            raise ZimbraClientException('Invalid request')

        return self.transport.invoke(ns,
                                     request_name,
                                     params,
                                     self.auth_token,
                                     simplify)


    @abc.abstractmethod
    def authenticate(self, account_name, password):
        """
        Authenticates zimbra account.
        @param account_name: account email address
        @param password: account password
        @raise AuthException: if authentication fails
        @raise SoapException: if soap communication fails
        """
