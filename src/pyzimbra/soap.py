# -*- coding: utf-8 -*-
"""
################################################################################
# Copyright (c) 2010, Ilgar Mashayev
# 
# E-mail: pyzimbra@lab.az
# Website: http://github.com/ilgarm/pyzimbra
################################################################################
# This file is part of pyzimbra.
# 
# Pyzimbra is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Pyzimbra is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with Pyzimbra.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

Soap related methods and classes.

@author: ilgar
"""
from pyzimbra import util, zconstant
from pyzimbra.base import ZimbraClientException
import urllib2


def admin_soap_url(hostname):
    """
    @return: absolute zimbra administrative soap endpoint url
    @raise SoapException: if hostname is empty
    """
    if util.empty(hostname):
        raise SoapException('Empty hostname')

    return 'https://%s%s' % (hostname, zconstant.SOAP_ADMIN_URL)


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
