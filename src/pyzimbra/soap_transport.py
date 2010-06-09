# -*- coding: utf-8 -*-
"""
Soap related methods and classes.

@author: ilgar
"""
from lxml import etree
from pyzimbra import zconstant, sconstant
from pyzimbra.base import ZimbraClientTransport
from pyzimbra.soap import SoapException
import gzip
import io
import urllib2


class SoapTransport(ZimbraClientTransport):
    """
    Soap transport.
    """
    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        ZimbraClientTransport.__init__(self)


    # ------------------------------------------------------------------ unbound
    def invoke(self, req, auth_token):
        """
        Invokes zimbra soap request.
        """
        env = self.wrap_soap_payload(req, auth_token)
        encoded = etree.tounicode(env)

        headers = { 'User-Agent': zconstant.USER_AGENT,
                   'Accept-encoding': 'gzip' }
        request = urllib2.Request(self.url, encoded, headers)
        response = urllib2.urlopen(request)
        data = response.read()

        if hasattr(response, 'headers'):
            if response.headers.get('content-encoding', '') == 'gzip':
                data = gzip.GzipFile(fileobj=io.StringIO(data)).read()

        return self.unwrap_soap_payload(data)


    def wrap_soap_payload(self, payload, auth_token = None):
        """
        Wraps zimbra xml request into soap envelope.
        @param payload: zimbra request
        @param auth_token: session to use to prepare soap authentication headers
        @return: soap envelope
        """
        env = etree.Element('%s%s' % (zconstant.NS_SOAP, sconstant.ENVELOPE),
                            nsmap=zconstant.NS_SOAP_MAP)

        header = etree.SubElement(env, '%s%s' % (zconstant.NS_SOAP,
                                                 sconstant.HEADER))
        header.clear()

        context = etree.SubElement(header, '%s%s' % (zconstant.NS_ZIMBRA,
                                                     sconstant.CONTEXT),
                                   nsmap=zconstant.NS_ZIMBRA_MAP)

        if auth_token != None:
            e = etree.SubElement(context, '%s%s' % (zconstant.NS_ZIMBRA,
                                                    sconstant.E_AUTH_TOKEN))
            e.text = auth_token.token

            e = etree.SubElement(context, '%s%s' % (zconstant.NS_ZIMBRA,
                                                    sconstant.E_SESSION_ID),
                                 attrib={sconstant.A_ID: auth_token.session_id})
            e.text = auth_token.session_id

        body = etree.SubElement(env, '%s%s' % (zconstant.NS_SOAP,
                                               sconstant.BODY))
        body.clear()
        body.insert(0, payload)

        return env


    def unwrap_soap_payload(self, str):
        """
        Unwraps soap envelope to zimbra xml response
        @param env: soap envelope
        @return: zimbra response
        @raise SoapException: if unable to identify soap body in response
        """ 
        env = etree.fromstring(str)

        # TODO process context
        body_list = env.xpath('/%s:%s/%s:%s/*[1]' % (zconstant.NS_SOAP_PREFIX,
                                               sconstant.ENVELOPE,
                                               zconstant.NS_SOAP_PREFIX,
                                               sconstant.BODY),
                               namespaces = zconstant.NS_SOAP_MAP)

        if len(body_list) == 0:
            raise SoapException('Unable to get soap body')

        return body_list[0]
