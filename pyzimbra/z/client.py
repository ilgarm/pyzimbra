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

Zimbra non-privileged client.

@author: ilgar
"""
from pyzimbra import sconstant, zconstant
from pyzimbra.z.zobject.account import AccountInfo
from pyzimbra.zclient import ZimbraSoapClient
import SOAPpy


class ZimbraClient(ZimbraSoapClient):
    """
    Zimbra non-privileged client.
    """
    # ------------------------------------------------------------------ unbound
    def authenticate(self, account_name, password):
        """
        Authenticates zimbra account.
        @param account_name: account email address
        @param password: account password
        @raise AuthException: if authentication fails
        @raise SoapException: if soap communication fails
        """
        self.auth_token = self.authenticator.authenticate(self.transport,
                                                          account_name,
                                                          password)


    def change_password(self, current_password, new_password):
        """
        Changes account password.
        @param current_password: current password
        @param new_password: new password
        """
        attrs = {sconstant.A_BY: sconstant.V_NAME}
        account = SOAPpy.Types.stringType(data=self.auth_token.account_name,
                                          attrs=attrs)

        params = {sconstant.E_ACCOUNT: account,
                  sconstant.E_OLD_PASSWORD: current_password,
                  sconstant.E_PASSWORD: new_password}

        self.invoke(zconstant.NS_ZIMBRA_ACC_URL,
                    sconstant.ChangePasswordRequest,
                    params)


    def get_account_info(self):
        """
        Gets account info.
        @return: AccountInfo
        """
        attrs = {sconstant.A_BY: sconstant.V_NAME}
        account = SOAPpy.Types.stringType(data=self.auth_token.account_name,
                                          attrs=attrs)

        params = {sconstant.E_ACCOUNT: account}

        res = self.invoke(zconstant.NS_ZIMBRA_ACC_URL,
                          sconstant.GetAccountInfoRequest,
                          params)

        info = AccountInfo()
        info.parse(res)

        return info


    def get_info(self, params={}):
        """
        Gets mailbox info.
        @param params: params to retrieve
        @return: AccountInfo
        """
        res = self.invoke(zconstant.NS_ZIMBRA_ACC_URL,
                          sconstant.GetInfoRequest,
                          params)

        return res
