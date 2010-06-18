# -*- coding: utf-8 -*-
"""
Soap related methods and classes.

@author: ilgar
"""
from lxml import etree
from pyzimbra import zconstant, sconstant
from pyzimbra.auth import AuthException, AuthToken, Authenticator
import urllib2


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
                                   attrib={sconstant.A_BY: sconstant.V_NAME})
        account.text = account_name

        passwd = etree.SubElement(req, sconstant.E_PASSWORD)
        passwd.text = password

        res = None
        try:
            res = transport.invoke(req, None)
        except urllib2.HTTPError as exc:
            e = AuthException('Authentication failed')
            e.__cause__ = exc
            raise e

        auth_token = AuthToken()
        auth_token.account_name = account_name
        auth_token.token = res.findtext('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                                  sconstant.E_AUTH_TOKEN))
        auth_token.session_id = res.findtext('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                                       sconstant.E_SESSION_ID))

        return auth_token
