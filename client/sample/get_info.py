# -*- coding: utf-8 -*-
"""
Account info samples.

@author: ilgar
"""
from lxml import etree
from pyzimbra import soap, sconstant, zconstant
from pyzimbra.soap_auth import SoapAuthenticator
from pyzimbra.soap_transport import SoapTransport
from pyzimbra.zclient import ZimbraClient
from sample.util import load_properties


def get_info():
    p = load_properties()

    auth = SoapAuthenticator()

    transport = SoapTransport()
    transport.url = soap.soap_url(p['hostname'])
    
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
    get_info()
