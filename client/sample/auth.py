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

Authentication samples.

@author: ilgar
"""
from client.util import load_properties
from pyzimbra import soap
from pyzimbra.base import ZimbraClientException
from pyzimbra.soap_auth import SoapAuthenticator
from pyzimbra.soap_transport import SoapTransport
from test import pconstant
import logging
import sys


def authenticate():
    p = load_properties()

    transport = SoapTransport()
    transport.soap_url = soap.soap_url(p[pconstant.HOSTNAME])

    auth = SoapAuthenticator()
    auth_token = auth.authenticate(transport,
                                   p[pconstant.ACCOUNT_NAME],
                                   p[pconstant.PASSWORD])

    print auth_token


def pre_authenticate():
    p = load_properties()

    transport = SoapTransport()
    transport.debug = 1
    transport.soap_url = soap.soap_url(p[pconstant.HOSTNAME])

    auth = SoapAuthenticator()
    auth.domains = p[pconstant.DOMAINS]
    auth_token = auth.authenticate(transport, p[pconstant.ACCOUNT_NAME])

    print auth_token


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)

    try:
        authenticate()
    except ZimbraClientException, e:
        e.print_trace()

    try:
        pre_authenticate()
    except ZimbraClientException, e:
        e.print_trace()
