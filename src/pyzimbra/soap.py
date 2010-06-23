# -*- coding: utf-8 -*-
"""
Soap related methods and classes.

@author: ilgar
"""
from pyzimbra import util, zconstant
from pyzimbra.base import ZimbraClientException
import urllib2


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
    # --------------------------------------------------------------- properties
    code = property(lambda self: self._code, 
                    lambda self, v: setattr(self, '_code', v))
    trace = property(lambda self: self._trace, 
                     lambda self, v: setattr(self, '_trace', v))

    # -------------------------------------------------------------------- bound
    def __init__(self, message, cause = None):
        ZimbraClientException.__init__(self, message, cause)

        self.code = None
        self.trace = None

        if cause != None and isinstance(cause, urllib2.HTTPError):
            self.code = cause.code


    def __unicode__(self):
        return '%s (%s:%s)' % (self.message, self.code, self.trace)
