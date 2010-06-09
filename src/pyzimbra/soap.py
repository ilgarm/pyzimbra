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


class SoapException(ZimbraClientException):
    """
    Soap exception.
    """
