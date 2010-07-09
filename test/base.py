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

@author: ilgar
"""
from test.util import load_test_properties


class BaseTest(object):

    # --------------------------------------------------------------- properties
    domain = property(lambda self: self._domain,
                      lambda self, v: setattr(self, '_domain', v))
    hostname = property(lambda self: self._hostname,
                        lambda self, v: setattr(self, '_hostname', v))
    domain_key = property(lambda self: self._domain_key,
                          lambda self, v: setattr(self, '_domain_key', v))

    username = property(lambda self: self._username,
                        lambda self, v: setattr(self, '_username', v))
    account_name = property(lambda self: self._account_name,
                            lambda self, v: setattr(self, '_account_name', v))
    account_id = property(lambda self: self._account_id,
                            lambda self, v: setattr(self, '_account_id', v))
    password = property(lambda self: self._password,
                        lambda self, v: setattr(self, '_password', v))
    token = property(lambda self: self._token,
                     lambda self, v: setattr(self, '_token', v))
    session_id = property(lambda self: self._session_id,
                          lambda self, v: setattr(self, '_session_id', v))


    # ------------------------------------------------------------------ unbound
    def setUp(self):
        load_test_properties(self)


    def tearDown(self):
        pass
