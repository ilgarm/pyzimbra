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

SOAPPy related methods and classes.

@author: ilgar
"""
from pyzimbra import zconstant, util
from pyzimbra.soap import SoapException
import SOAPpy
import logging
import urllib2
import xml.sax


class ZimbraSOAPParser(SOAPpy.SOAPParser):
    """
    No need to keep track of hrefs for zimbra.
    Ugliest hack ever: just empty list of ref ids every time.
    Could not find another workaround.
    """
    # -------------------------------------------------------------------- bound
    def __init__(self, rules = None):
        SOAPpy.SOAPParser.__init__(self, rules)


    # ------------------------------------------------------------------ unbound
    def endElementNS(self, name, qname):
        self._ids = {}
        SOAPpy.SOAPParser.endElementNS(self, name, qname)


def parseSOAP(xml_str, rules = None):
    """
    Replacement for SOAPpy._parseSOAP method to spoof SOAPParser.
    """
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

    parser = xml.sax.make_parser()
    t = ZimbraSOAPParser(rules = rules)
    parser.setContentHandler(t)
    e = xml.sax.handler.ErrorHandler()
    parser.setErrorHandler(e)

    inpsrc = xml.sax.xmlreader.InputSource()
    inpsrc.setByteStream(StringIO(xml_str))

    # turn on namespace mangeling
    parser.setFeature(xml.sax.handler.feature_namespaces,1)

    try:
        parser.parse(inpsrc)
    except xml.sax.SAXParseException, e:
        parser._parser = None
        raise e

    return t


class SoapHttpTransport(SOAPpy.Client.HTTPTransport):
    """
    Http transport using urllib2, with support for proxy authentication and more.
    """
    # --------------------------------------------------------------- properties
    transport = property(lambda self: self._transport,
                         lambda self, v: setattr(self, '_transport', v))


    # -------------------------------------------------------------------- bound
    def __init__(self):
        self.log = logging.getLogger(__name__)


    # ------------------------------------------------------------------ unbound
    def call(self, addr, data, namespace, soapaction = None, encoding = None,
        http_proxy = None, config = SOAPpy.Config):

        if not isinstance(addr, SOAPpy.Client.SOAPAddress):
            addr = SOAPpy.Client.SOAPAddress(addr, config)

        url = addr.proto + "://" + addr.host + addr.path

        headers = {'User-Agent': zconstant.USER_AGENT}
        request = urllib2.Request(url, data, headers)

        self.log.debug('Request url: %s' % url)
        self.log.debug('Request headers')
        self.log.debug(request.headers)
        self.log.debug('Request data')
        self.log.debug(data)

        try:
            opener = self.build_opener()
            response = opener.open(request)
            data = response.read()

            self.log.debug('Response headers')
            self.log.debug(response.headers)
            self.log.debug('Response data')
            self.log.debug(data)

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
                self.log.debug(data)

                t = SOAPpy.Parser.parseSOAP(data)
                message = '%s:%s' % (t.Fault.faultcode, t.Fault.faultstring)
                e = SoapException(message, exc)
                e.code = t.Fault.detail.Error.Code
                e.trace = t.Fault.detail.Error.Trace
                return e
            except:
                return SoapException(unicode(exc), exc)

        return SoapException(exc.reason, exc)
