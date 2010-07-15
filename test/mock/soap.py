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

Soap related mockups.

@author: ilgar
"""
from pyzimbra.base import ZimbraClientTransport
from pyzimbra.soap import SoapException
from test.mock import responses
from test.util import load_test_properties


class MockTransport(ZimbraClientTransport):
    """
    Mocked transport.
    """
    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        ZimbraClientTransport.__init__(self)

        load_test_properties(self)


    # ------------------------------------------------------------------ unbound
    def invoke(self, ns, request_name, params, auth_token, simplify=False):

        if auth_token.token == None:
            auth_token.token = self.token
            auth_token.session_id = self.session_id

        return responses.get_response(request_name, params, auth_token)


class MockFailingTransport(ZimbraClientTransport):
    """
    Mocked failing transport.
    """
    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        ZimbraClientTransport.__init__(self)

        load_test_properties(self)


    # ------------------------------------------------------------------ unbound
    def invoke(self, ns, request_name, params, auth_token):
        raise SoapException('Mocked Error')
