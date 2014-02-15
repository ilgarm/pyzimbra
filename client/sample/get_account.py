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

Account info samples.

@author: ilgar
"""
from client.util import load_properties
from pyzimbra import sconstant, zconstant, soap
from pyzimbra.z.admin import ZimbraAdmin
from test import pconstant
import SOAPpy
import logging
import sys


def get_account():
    p = load_properties()

    zclient = ZimbraAdmin(soap.admin_soap_url(p[pconstant.ADMIN_HOSTNAME]))
    zclient.authenticate(p[pconstant.ADMIN_ACCOUNT_NAME],
                         p[pconstant.ADMIN_PASSWORD])

    attrs = {sconstant.A_BY: sconstant.V_NAME}
    account = SOAPpy.Types.stringType(data=p[pconstant.ACCOUNT_NAME], attrs=attrs)

    params = {sconstant.E_ACCOUNT: account}
    res = zclient.invoke(zconstant.NS_ZIMBRA_ADMIN_URL,
                         sconstant.GetAccountRequest,
                         params)

    print res


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)

    get_account()
