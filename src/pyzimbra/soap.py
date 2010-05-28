# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from pyzimbra import zconstant, sconstant
import urllib2
import gzip
import io
from lxml import etree


def send_request(url, req):
    """
    Sends request to zimbra endpoint and extracts payload
    """
    env = prepare_soap_envelope(req)

    encoded = env
    headers = { 'User-Agent' : zconstant.USER_AGENT,
               'Accept-encoding' : 'gzip' }
    request = urllib2.Request(url, encoded, headers)
    response = urllib2.urlopen(request)
    data = response.read()

    if hasattr(response, 'headers'):
        if response.headers.get('content-encoding', '') == 'gzip':
            data = gzip.GzipFile(fileobj=io.StringIO(data)).read()

    return data


def prepare_soap_envelope(payload):
    """
    Wraps zimbra xml request into soap envelope
    @param payload: zimbra xml request
    """
    env = etree.Element(zconstant.NS_SOAP + sconstant.ENVELOPE,
                             nsmap=zconstant.NS_SOAP_MAP)
    header = etree.SubElement(env, zconstant.NS_SOAP + sconstant.HEADER)
    body = etree.SubElement(env, zconstant.NS_SOAP + sconstant.BODY)

    context = etree.SubElement(header, sconstant.CONTEXT,
                                    nsmap=zconstant.NS_ZIMBRA_MAP)

    body.clear()
    body.insert(0, payload)

    return etree.tounicode(env, pretty_print=True)


def prepare_auth_request(domain, username, password):
    """
    Prepares zimbra auth request
    """
    req = etree.Element(sconstant.AuthRequest,
                             nsmap=zconstant.NS_ZIMBRA_ACC_MAP)

    account = etree.SubElement(req, sconstant.E_ACCOUNT,
                                    attrib={sconstant.A_BY: sconstant.A_NAME})
    account.text = username

    passwd = etree.SubElement(req, sconstant.E_PASSWORD)
    passwd.text = password

    vhost = etree.SubElement(req, sconstant.E_VHOST)
    vhost.text = domain

    return req


