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
from pyzimbra import zconstant, sconstant
from pyzimbra.base import ZimbraClientTransport
from pyzimbra.soap_soappy import parseSOAP, SoapHttpTransport
import SOAPpy
import logging


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
        self.log = logging.getLogger(__name__)


    # ------------------------------------------------------------------ unbound
    def invoke(self, ns, request_name, params, auth_token, simplify=False):
        """
        Invokes zimbra soap request.
        """
        ZimbraClientTransport.invoke(self,
                                     ns,
                                     request_name,
                                     params,
                                     auth_token,
                                     simplify)

        headers = SOAPpy.Types.headerType()

        if auth_token.token != None:
            data={sconstant.E_AUTH_TOKEN: auth_token.token,
                  sconstant.E_SESSION_ID: auth_token.session_id}
            context = SOAPpy.Types.structType(data=data, name=sconstant.CONTEXT)
            context._validURIs = []
            context._ns = (zconstant.SOAP_DEFAULT_PREFIX, zconstant.NS_ZIMBRA_URL)
            headers.context = context

        proxy = SOAPpy.SOAPProxy(self.soap_url,
                                 ns,
                                 header=headers,
                                 noroot=1,
                                 simplify_objects=simplify)
        proxy.config.debug = self.log.isEnabledFor(logging.DEBUG)
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
