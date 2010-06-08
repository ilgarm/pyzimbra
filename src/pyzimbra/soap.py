# -*- coding: utf-8 -*-
"""
Soap related methods and classes.

@author: ilgar
"""
from lxml import etree
from pyzimbra import zconstant, sconstant, util
from pyzimbra.auth import AuthException, AuthToken, Authenticator
from pyzimbra.base import ZimbraClientException, ZimbraClientTransport
import gzip
import io
import urllib2


class SoapException(ZimbraClientException):
    """
    Soap exception.
    """


def soap_url(hostname):
    """
    @return: absolute zimbra soap endpoint url
    @raise SoapException: if hostname is empty
    """
    if util.empty(hostname):
            raise SoapException('Empty hostname')

    return 'http://%s%s' % (hostname, zconstant.SOAP_URL)


def wrap_soap_payload(payload):
    """
    Wraps zimbra xml request into soap envelope.
    @param payload: zimbra request
    @return: soap envelope
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


class SoapTransport(ZimbraClientTransport):
    """
    Soap transport.
    """
    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        ZimbraClientTransport.__init__(self)


    # ------------------------------------------------------------------ unbound
    def invoke(self, req):
        """
        Invokes zimbra request.
        @param req: request to invoke
        @return: zimbra response
        """
        env = wrap_soap_payload(req)
        encoded = etree.tounicode(env)

        headers = { 'User-Agent': zconstant.USER_AGENT,
                   'Accept-encoding': 'gzip' }
        request = urllib2.Request(self.url, encoded, headers)
        response = urllib2.urlopen(request)
        data = response.read()

        if hasattr(response, 'headers'):
            if response.headers.get('content-encoding', '') == 'gzip':
                data = gzip.GzipFile(fileobj=io.StringIO(data)).read()

        return unwrap_soap_payload(data)


class SoapAuthenticator(Authenticator):
    """
    Soap authenticator.
    """
    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        Authenticator.__init__(self)

    # ------------------------------------------------------------------ unbound
    def authenticate(self, transport, account_name, password):
        """
        Authenticates account using soap method.
        """
        Authenticator.authenticate(self, transport, account_name, password)

        req = etree.Element(sconstant.AuthRequest,
                            nsmap=zconstant.NS_ZIMBRA_ACC_MAP)

        account = etree.SubElement(req, sconstant.E_ACCOUNT,
                                   attrib={sconstant.A_BY: sconstant.A_NAME})
        account.text = account_name

        passwd = etree.SubElement(req, sconstant.E_PASSWORD)
        passwd.text = password

        res = None
        try:
            res = transport.invoke(req)
        except urllib2.HTTPError:
            raise AuthException('Authentication failed')

        auth_token = AuthToken()
        auth_token.token = res.findtext('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                                  sconstant.E_AUTH_TOKEN))
        auth_token.session_id = res.findtext('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                                       sconstant.E_SESSION_ID))

        return auth_token
