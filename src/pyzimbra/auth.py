# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from lxml import etree
from pyzimbra import util, zutil, soap, sconstant, zconstant, soap_transport
from pyzimbra.zutil import ZClientException
from xml.dom import minidom
import urllib2


class AuthException(ZClientException):
    """
    Authentication exception.
    """


class AuthToken(object):
    """
    AuthToken holds current authentication token and sessions id.
    """
    token = property(lambda self: self._token,
                     lambda self, v: setattr(self, '_token', v))
    session_id = property(lambda self: self._session_id,
                          lambda self, v: setattr(self, '_session_id', v))


    def __init__(self):
        """
        Constructor
        """


class Authenticator(object):
    """
    Authenticator provides methods to authenticate using username/password 
    as a user or administrator or using domain key.
    """
    # --------------------------------------------------------------- properties
    hostname = property(lambda self: self._hostname,
                        lambda self, v: setattr(self, '_hostname', v))
    domain = property(lambda self: self._domain,
                      lambda self, v: setattr(self, '_domain', v))
    domain_key = property(lambda self: self._domain_key,
                          lambda self, v: setattr(self, '_domain_key', v))
    username = property(lambda self: self._username,
                        lambda self, v: setattr(self, '_username', v))
    password = property(lambda self: self._password,
                        lambda self, v: setattr(self, '_password', v))

    # -------------------------------------------------------------------- bound
    def __init__(self):
        """
        Constructor
        """

    # ------------------------------------------------------------------ unbound
    def authenticate(self, username, password):
        """
        Authenticates account.
        
        @param username: account name, can be local part or full email
        @param password: account password
        
        @raise AuthException: if authentication fails
        @return: AuthToken if authentication succeeded
        """
        if util.empty(username):
            raise AuthException('Empty username')

        if util.empty(password):
            raise AuthException('Empty password')

        url = zutil.soap_url(self.hostname)

        req = etree.Element(sconstant.AuthRequest,
                            nsmap=zconstant.NS_ZIMBRA_ACC_MAP)

        account = etree.SubElement(req, sconstant.E_ACCOUNT,
                                   attrib={sconstant.A_BY: sconstant.A_NAME})
        account.text = '%s@%s' % (username, self.domain)

        passwd = etree.SubElement(req, sconstant.E_PASSWORD)
        passwd.text = password

        vhost = etree.SubElement(req, sconstant.E_VHOST)
        vhost.text = self.hostname

        res = None
        try:
            res = soap_transport.send_request(url, req)
        except urllib2.HTTPError:
            raise AuthException('Authentication failed')

        xmldoc = minidom.parseString(etree.tostring(res))
        xmldoc.getElementsByTagNameNS(zconstant.NS_ZIMBRA_ACC_URL,
                                      sconstant.AuthResponse)

        token = AuthToken()

        node = xmldoc.getElementsByTagName(sconstant.E_AUTH_TOKEN)
        token.token = getText(node[0].childNodes)

        node = xmldoc.getElementsByTagName(sconstant.E_SESSION_ID)
        token.session_id = getText(node[0].childNodes)

        return token

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)
