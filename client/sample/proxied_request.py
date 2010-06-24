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
from lxml import etree
from pyzimbra import soap, sconstant, zconstant
from pyzimbra.soap_auth import SoapAuthenticator
from pyzimbra.soap_transport import SoapTransport
from pyzimbra.zclient import ZimbraClient
from sample.util import load_properties


def get_proxied_info():
    p = load_properties()

    auth = SoapAuthenticator()

    transport = SoapTransport()
    transport.url = soap.soap_url(p['hostname'])
    transport.proxy_url = soap.proxy_url(p['proxy_hostname'],
                                         p['proxy_username'],
                                         p['proxy_password'],
                                         p['proxy_port'],
                                         p['proxy_scheme'])

    zclient = ZimbraClient()
    zclient.transport = transport

    zclient.authenticate(auth, p['account_name'], p['password'])

    req = etree.Element(sconstant.GetInfoRequest,
                        attrib={sconstant.A_SECTIONS: sconstant.V_MBOX},
                        nsmap=zconstant.NS_ZIMBRA_ACC_MAP)
    res = zclient.invoke(req)

    account_name = res.findtext('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                          sconstant.E_NAME))

    print account_name
    print etree.tostring(res)


if __name__ == '__main__':
    get_proxied_info()
