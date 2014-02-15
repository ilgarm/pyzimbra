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
import pconstant


def load_test_properties(test):
    cfg = ConfigParser()
    if len(cfg.read("test.properties")) == 0:
        cfg.read("../test.properties")

    test.admin_hostname = cfg.get(pconstant.ADMIN, pconstant.HOST)
    test.admin_account_name = cfg.get(pconstant.ADMIN, pconstant.USERNAME)
    test.admin_password = cfg.get(pconstant.ADMIN, pconstant.PASSWORD)

    test.domain = cfg.get(pconstant.DOMAIN, pconstant.NAME)
    test.hostname = cfg.get(pconstant.DOMAIN, pconstant.HOST)
    test.domain_key = cfg.get(pconstant.DOMAIN, pconstant.KEY)

    test.username = cfg.get(pconstant.AUTH, pconstant.USERNAME)
    test.account_name = '%s@%s' % (test.username, test.domain)
    test.account_id = cfg.get(pconstant.AUTH, pconstant.ID)
    test.password = cfg.get(pconstant.AUTH, pconstant.PASSWORD)
    test.token = cfg.get(pconstant.AUTH, pconstant.TOKEN)
    test.session_id = cfg.get(pconstant.AUTH, pconstant.SESSION_ID)
