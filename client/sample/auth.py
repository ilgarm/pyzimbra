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
from pyzimbra import soap
from pyzimbra.soap_auth import SoapAuthenticator
from pyzimbra.soap_transport import SoapTransport
from sample.util import load_properties
from pyzimbra.base import ZimbraClientException


def authenticate():
    p = load_properties()

    auth = SoapAuthenticator()
    transport = SoapTransport()

    transport.url = soap.soap_url(p['hostname'])

    auth_token = auth.authenticate(transport, p['account_name'], p['password'])

    print auth_token.token


if __name__ == '__main__':
    try:
        authenticate()
    except ZimbraClientException, e:
        e.print_trace()
