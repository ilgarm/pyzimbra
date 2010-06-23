# -*- coding: utf-8 -*-
"""
Soap related methods and classes.

@author: ilgar
"""
from lxml import etree
from pyzimbra import zconstant, sconstant, util
from pyzimbra.base import ZimbraClientTransport
from pyzimbra.soap import SoapException
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

        headers = {'User-Agent': zconstant.USER_AGENT}
        request = urllib2.Request(self.url, encoded, headers)

        try:
            opener = self.build_opener()
            response = opener.open(request)
            data = response.read()
        except urllib2.URLError as exc:
            raise self.init_soap_exception(exc)

        return self.unwrap_soap_payload(data)


    def build_opener(self):
        """
        Builds url opener, initializing proxy with auth if required.
        @return: OpenerDirector
        """
        if util.empty(self.proxy_url):
            return urllib2.build_opener()

        proxy_handler = urllib2.ProxyHandler({self.proxy_url[:4]: self.proxy_url})

        return urllib2.build_opener(proxy_handler)


    def init_soap_exception(self, exc):
        """
        Initializes exception based on soap error response.
        @param exc: URLError
        @return: SoapException
        """
        if not isinstance(exc, urllib2.HTTPError):
            return SoapException(unicode(exc), exc)

        if isinstance(exc, urllib2.HTTPError):
            try:
                return self.unwrap_soap_exception(exc)
            except:
                return SoapException(unicode(exc), exc)

        return SoapException(exc.reason, exc)


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


    def unwrap_soap_exception(self, exc):
        """
        Unwraps soap exception and instantiates python exception object.
        @param exc: HTTPError
        @return: SoapException
        """
        env = etree.fromstring(exc.read())

        body_list = env.xpath('/%s:%s/%s:%s/%s:%s/%s:%s/%s:%s'
                              % (zconstant.NS_SOAP_PREFIX,
                                 sconstant.ENVELOPE,
                                 zconstant.NS_SOAP_PREFIX,
                                 sconstant.BODY,
                                 zconstant.NS_SOAP_PREFIX,
                                 sconstant.FAULT,
                                 zconstant.NS_SOAP_PREFIX,
                                 sconstant.REASON,
                                 zconstant.NS_SOAP_PREFIX,
                                 sconstant.TEXT),
                               namespaces = zconstant.NS_SOAP_MAP)

        message = body_list[0].text

        body_list = env.xpath('/%s:%s/%s:%s/%s:%s/%s:%s/*[1]'
                              % (zconstant.NS_SOAP_PREFIX,
                                 sconstant.ENVELOPE,
                                 zconstant.NS_SOAP_PREFIX,
                                 sconstant.BODY,
                                 zconstant.NS_SOAP_PREFIX,
                                 sconstant.FAULT,
                                 zconstant.NS_SOAP_PREFIX,
                                 sconstant.DETAIL),
                               namespaces = zconstant.NS_SOAP_MAP)

        code = body_list[0].findtext('%s%s' % (zconstant.NS_ZIMBRA,
                                               sconstant.E_CODE))
        trace = body_list[0].findtext('%s%s' % (zconstant.NS_ZIMBRA,
                                                sconstant.E_TRACE))

        e = SoapException(message, exc)
        e.code = code
        e.trace = trace
        return e
