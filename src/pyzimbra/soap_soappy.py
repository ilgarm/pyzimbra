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
import SOAPpy
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
    Replacement for soappy parseSOAP method to spoof SOAPParser.
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
