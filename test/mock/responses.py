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

Zimbra request and response mocked values.

@author: ilgar
"""
from pyzimbra import sconstant
from pyzimbra.soap_soappy import parseSOAP
import SOAPpy



CHANGE_TOKEN = 12704
LIFETIME = 86400000

def init_soap_parser(f):
    def call(params, auth_token):
        _parseSOAP = SOAPpy.Parser._parseSOAP
        SOAPpy.Parser._parseSOAP = parseSOAP
        try:
            return f(params, auth_token)
        finally:
            SOAPpy.Parser._parseSOAP = _parseSOAP
    return call


def get_response(request_name, params, auth_token):

    if request_name == sconstant.AuthRequest:
        return AuthResponse(params, auth_token)

    if request_name == sconstant.GetInfoRequest:
        return GetInfoResponse(params, auth_token)

    return None


@init_soap_parser
def AuthResponse(params, auth_token):

    str = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Header>
    <context xmlns="urn:zimbra">
    <sessionId id="%(session_id)s">%(session_id)s</sessionId>
    <refresh>
    <version>%(version)s</version>
    </refresh>
    <change token="%(change_token)s"/>
    </context>
    </soap:Header>
    <soap:Body>
    <AuthResponse xmlns="urn:zimbraAccount">
    <authToken>%(token)s</authToken>
    <lifetime>%(lifetime)s</lifetime>
    <sessionId id="%(session_id)s">%(session_id)s</sessionId>
    </AuthResponse>
    </soap:Body>
    </soap:Envelope>
    """
    str = str % {'version': '5.0 VGDU1296_local 20091028-1850',
                 'change_token': CHANGE_TOKEN,
                 'lifetime': LIFETIME,
                 'token': auth_token.token,
                 'session_id': auth_token.session_id}

    return SOAPpy.Parser.parseSOAP(str).AuthResponse


@init_soap_parser
def GetInfoResponse(params, auth_token):
    
    str = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Header>
    <context xmlns="urn:zimbra">
    <sessionId id="%(session_id)s">%(session_id)s</sessionId>
    <change token="%(change_token)s"/>
    </context>
    </soap:Header>
    <soap:Body>
    <GetInfoResponse xmlns="urn:zimbraAccount">
    <version>%(version)s</version>
    <name>%(account_name)s</name>
    <lifetime>%(lifetime)s</lifetime>
    </GetInfoResponse>
    </soap:Body>
    </soap:Envelope>
    """
    str = str % {'version': '5.0 VGDU1296_local 20091028-1850',
                 'change_token': CHANGE_TOKEN,
                 'lifetime': LIFETIME,
                 'token': auth_token.token,
                 'session_id': auth_token.session_id,
                 'account_name': auth_token.account_name}

    return SOAPpy.Parser.parseSOAP(str).GetInfoResponse
