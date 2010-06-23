# -*- coding: utf-8 -*-
"""
Soap related methods and classes.

@author: ilgar
"""
from pyzimbra import util, zconstant
from pyzimbra.base import ZimbraClientException


def soap_url(hostname):
    """
    @return: absolute zimbra soap endpoint url
    @raise SoapException: if hostname is empty
    """
    if util.empty(hostname):
            raise SoapException('Empty hostname')

    return 'http://%s%s' % (hostname, zconstant.SOAP_URL)


def proxy_url(hostname, username=None, password=None, port=0, scheme='http'):
    """
    @return: absolute proxy url
    @raise SoapException: if scheme or hostname is empty
    """
    if util.empty(hostname):
            raise SoapException('Empty hostname')

    if util.empty(scheme):
            raise SoapException('Empty scheme')

    hostport = hostname
    if port > 0 and (scheme != 'http' or port != 80):
        hostport = '%s:%s' % (hostname, port)

    userpass = ''
    if not util.empty(username):
        userpass = '%s:%s@' % (username, password)

    url = '%s://%s%s' % (scheme, userpass, hostport)

    return url


class SoapException(ZimbraClientException):
    """
    Soap exception.
    """
    # -------------------------------------------------------------------- bound
    def __init__(self, message, cause = None):
        ZimbraClientException.__init__(self, message, cause)
