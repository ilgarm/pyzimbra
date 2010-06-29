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

Test related methods and classes.

@author: ilgar
"""
from ConfigParser import ConfigParser


def load_test_properties(test):
    cfg = ConfigParser()
    if len(cfg.read("test.properties")) == 0:
        cfg.read("../test.properties")

    test.domain = cfg.get("domain", "name")
    test.hostname = cfg.get("domain", "host")
    test.domain_key = cfg.get("domain", "key")

    test.username = cfg.get("auth", "username")
    test.account_name = '%s@%s' % (test.username, test.domain)
    test.account_id = cfg.get("auth", "id")
    test.password = cfg.get("auth", "password")
    test.token = cfg.get("auth", "token")
    test.session_id = cfg.get("auth", "session_id")
