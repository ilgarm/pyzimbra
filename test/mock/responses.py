# -*- coding: utf-8 -*-
"""
Zimbra request and response mocked values.

@author: ilgar
"""
from lxml import etree
from pyzimbra import sconstant, zconstant


def get_response(req, auth_token):

    if req.tag == sconstant.AuthRequest:
        return AuthResponse(req, auth_token)

    if req.tag == sconstant.GetInfoRequest:
        return GetInfoResponse(req, auth_token)

    return None


def AuthResponse(req, auth_token):

    res = etree.Element('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                  sconstant.AuthResponse),
                        nsmap=zconstant.NS_ZIMBRA_ACC_MAP)

    e = etree.SubElement(res, '%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                        sconstant.E_AUTH_TOKEN))
    e.text = auth_token.token

    e = etree.SubElement(res, '%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                        sconstant.E_SESSION_ID),
                         attrib={sconstant.A_ID: auth_token.session_id})
    e.text = auth_token.session_id

    return res


def GetInfoResponse(req, auth_token):
    res = etree.Element('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                  sconstant.GetInfoResponse),
                        nsmap=zconstant.NS_ZIMBRA_ACC_MAP)

    e = etree.SubElement(res, '%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                        sconstant.E_NAME))
    e.text = auth_token.account_name

    return res
