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
from pyzimbra import zconstant, sconstant, util
from pyzimbra.base import ZimbraClientTransport
from pyzimbra.soap import SoapException
from pyzimbra.soap_soappy import parseSOAP
import SOAPpy
import urllib2


class SoapHttpTransport(SOAPpy.Client.HTTPTransport):
    """
    Http transport using urllib2, with support for proxy authentication and more.
    """
    # --------------------------------------------------------------- properties
    transport = property(lambda self: self._transport,
                   lambda self, v: setattr(self, '_transport', v))


    # ------------------------------------------------------------------ unbound
    def call(self, addr, data, namespace, soapaction = None, encoding = None,
        http_proxy = None, config = SOAPpy.Config):

        if not isinstance(addr, SOAPpy.Client.SOAPAddress):
            addr = SOAPpy.Client.SOAPAddress(addr, config)

        headers = {'User-Agent': zconstant.USER_AGENT}
        request = urllib2.Request(self.transport.url, data, headers)

        if self.transport.debug == 1:
            print 'Request url: ', self.transport.url
            print 'Request headers: '
            print request.headers
            print 'Request data: '
            print data

        try:
            opener = self.build_opener()
            response = opener.open(request)
            data = response.read()

            if self.transport.debug == 1:
                print 'Response headers: '
                print response.headers
                print 'Response data: '
                print data

        except urllib2.URLError as exc:
            raise self.init_soap_exception(exc)

        # get the new namespace
        if namespace is None:
            new_ns = None
        else:
            new_ns = self.getNS(namespace, data)

        return data, new_ns


    def build_opener(self):
        """
        Builds url opener, initializing proxy.
        @return: OpenerDirector
        """
        http_handler = urllib2.HTTPHandler() # debuglevel=self.transport.debug

        if util.empty(self.transport.proxy_url):
            return urllib2.build_opener(http_handler)

        proxy_handler = urllib2.ProxyHandler(
            {self.transport.proxy_url[:4]: self.transport.proxy_url})

        return urllib2.build_opener(http_handler, proxy_handler)


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
                data = exc.read()
                if self.transport.debug == 1:
                    print data

                t = SOAPpy.Parser.parseSOAP(data)
                message = '%s:%s' % (t.Fault.faultcode, t.Fault.faultstring)
                e = SoapException(message, exc)
                e.code = t.Fault.detail.Error.Code
                e.trace = t.Fault.detail.Error.Trace
                return e
            except:
                return SoapException(unicode(exc), exc)

        return SoapException(exc.reason, exc)


class SoapTransport(ZimbraClientTransport):
    """
    Soap transport.
    """
    # --------------------------------------------------------------- properties
    http_transport = SoapHttpTransport()


    # -------------------------------------------------------------------- bound
    def __init__(self):
        ZimbraClientTransport.__init__(self)
        self.http_transport.transport = self


    # ------------------------------------------------------------------ unbound
    def invoke(self, ns, request_name, params, auth_token):
        """
        Invokes zimbra soap request.
        """
        headers = SOAPpy.Types.headerType()

        if auth_token != None:
            data={sconstant.E_AUTH_TOKEN: auth_token.token,
                  sconstant.E_SESSION_ID: auth_token.session_id}
            context = SOAPpy.Types.structType(data=data, name=sconstant.CONTEXT)
            context._validURIs = []
            context._ns = ("ns1", zconstant.NS_ZIMBRA_URL)
            headers.context = context

        proxy = SOAPpy.SOAPProxy(self.url, ns, header=headers, noroot=1)
        proxy.config.debug = self.debug
        proxy.config.strictNamespaces = 0
        proxy.config.buildWithNamespacePrefix = 0
        proxy.transport = self.http_transport

        _parseSOAP = SOAPpy.Parser._parseSOAP
        SOAPpy.Parser._parseSOAP = parseSOAP
        try:
            m = proxy.__getattr__(request_name)
            return m.__call__(**params)
        finally:
            SOAPpy.Parser._parseSOAP = _parseSOAP
