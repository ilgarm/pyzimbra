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
from pyzimbra import zconstant, sconstant, util, pconstant
from pyzimbra.auth import AuthException, AuthToken, Authenticator
from pyzimbra.soap import SoapException
from time import time
import SOAPpy
import hashlib
import hmac

class SoapAuthenticator(Authenticator):
    """
    Soap authenticator.
    """
    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        Authenticator.__init__(self)

    # ------------------------------------------------------------------ unbound
    def authenticate(self, transport, account_name, password=None):
        """
        Authenticates account using soap method.
        """
        Authenticator.authenticate(self, transport, account_name, password)

        if password == None:
            return self.pre_auth(transport, account_name)
        else:
            return self.auth(transport, account_name, password)


    def auth(self, transport, account_name, password):
        """
        Authenticates using username and password.
        """
        auth_token = AuthToken()
        auth_token.account_name = account_name

        attrs = {sconstant.A_BY: sconstant.V_NAME}
        account = SOAPpy.Types.stringType(data=account_name, attrs=attrs)

        params = {sconstant.E_ACCOUNT: account,
                  sconstant.E_PASSWORD: password}
        try:
            res = transport.invoke(zconstant.NS_ZIMBRA_ACC_URL,
                                   sconstant.AuthRequest,
                                   params,
                                   auth_token)
        except SoapException as exc:
            raise AuthException(unicode(exc), exc)

        auth_token.token = res.authToken
        auth_token.session_id = res.sessionId

        return auth_token


    def pre_auth(self, transport, account_name):
        """
        Authenticates using username and domain key.
        """
        auth_token = AuthToken()
        auth_token.account_name = account_name

        domain = util.get_domain(account_name)
        if domain == None:
            raise AuthException('Invalid auth token account')

        if domain in transport.domains and pconstant.KEY in transport.domains[domain]:
            domain_key = transport.domains[domain][pconstant.KEY]
        else:
            domain_key = None

        if domain_key == None:
            raise AuthException('Invalid domain key for domain %s' % domain)

        expires = 0
        timestamp = int(time() * 1000)
        pak = hmac.new(domain_key, '%s|%s|%s|%s' %
                       (account_name, sconstant.E_NAME, expires, timestamp),
                       hashlib.sha1).hexdigest()

        attrs = {sconstant.A_BY: sconstant.V_NAME}
        account = SOAPpy.Types.stringType(data=account_name, attrs=attrs)

        attrs = {sconstant.A_TIMESTAMP: timestamp, sconstant.A_EXPIRES: expires}
        preauth = SOAPpy.Types.stringType(data=pak,
                                          name=sconstant.E_PREAUTH,
                                          attrs=attrs)

        params = {sconstant.E_ACCOUNT: account,
                  sconstant.E_PREAUTH: preauth}
        try:
            res = transport.invoke(zconstant.NS_ZIMBRA_ACC_URL,
                                   sconstant.AuthRequest,
                                   params,
                                   auth_token)
        except SoapException as exc:
            raise AuthException(unicode(exc), exc)

        auth_token.token = res.authToken
        auth_token.session_id = res.sessionId

        return auth_token
