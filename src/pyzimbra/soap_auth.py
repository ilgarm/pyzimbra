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
from lxml import etree
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

        req = etree.Element(sconstant.AuthRequest,
                            nsmap=zconstant.NS_ZIMBRA_ACC_MAP)

        account = etree.SubElement(req, sconstant.E_ACCOUNT,
                                   attrib={sconstant.A_BY: sconstant.V_NAME})
        account.text = account_name

        passwd = etree.SubElement(req, sconstant.E_PASSWORD)
        passwd.text = password

        res = None
        try:
            res = transport.invoke(req, None)
        except SoapException as exc:
            raise AuthException(unicode(exc), exc)

        auth_token = AuthToken()
        auth_token.account_name = account_name
        auth_token.token = res.findtext('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                                  sconstant.E_AUTH_TOKEN))
        auth_token.session_id = res.findtext('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                                       sconstant.E_SESSION_ID))

        return auth_token
