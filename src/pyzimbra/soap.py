# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from lxml import etree
from pyzimbra import zconstant, sconstant
from pyzimbra.zutil import ZClientException
import lxml


class SoapException(ZClientException):
    """
    Soap exception.
    """


def wrap_soap_payload(payload):
    """
    Wraps zimbra xml request into soap envelope
    @param payload: zimbra xml request
    """
    env = etree.Element('%s%s' % (zconstant.NS_SOAP, sconstant.ENVELOPE),
                        nsmap=zconstant.NS_SOAP_MAP)

#    header = 
    etree.SubElement(env, zconstant.NS_SOAP + sconstant.HEADER)
    body = etree.SubElement(env, zconstant.NS_SOAP + sconstant.BODY)

    # TODO process context
#    context = etree.SubElement(header, sconstant.CONTEXT,
#                               nsmap=zconstant.NS_ZIMBRA_MAP)

    body.clear()
    body.insert(0, payload)

    return env


def unwrap_soap_payload(str):
    """
    Unwraps soap envelope to zimbra xml response
    @param env: soap envelope
    """ 
    env = lxml.etree.fromstring(str)

    # TODO process context
    body_list = env.xpath('/%s:%s/%s:%s/*[1]' % (zconstant.NS_SOAP_PREFIX,
                                           sconstant.ENVELOPE,
                                           zconstant.NS_SOAP_PREFIX,
                                           sconstant.BODY),
                           namespaces = zconstant.NS_SOAP_MAP)

    if len(body_list) == 0:
        raise SoapException('Unable to get soap body')

    return body_list[0]
