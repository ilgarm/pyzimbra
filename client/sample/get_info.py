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
from client.sample.util import load_properties
from pyzimbra import sconstant, zconstant, soap
from pyzimbra.soap_auth import SoapAuthenticator
from pyzimbra.soap_transport import SoapTransport
from pyzimbra.zclient import ZimbraClient
from test import pconstant
import logging
import sys


def get_info():
    p = load_properties()

    transport = SoapTransport()
    transport.soap_url = soap.soap_url(p[pconstant.HOSTNAME])

    auth = SoapAuthenticator()

    zclient = ZimbraClient()
    zclient.transport = transport

    zclient.authenticate(auth, p[pconstant.ACCOUNT_NAME], p[pconstant.PASSWORD])

    params = {sconstant.A_SECTIONS: sconstant.V_MBOX}
    res = zclient.invoke(zconstant.NS_ZIMBRA_ACC_URL,
                         sconstant.GetInfoRequest,
                         params)

    print res
    print res.name


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)

    get_info()
