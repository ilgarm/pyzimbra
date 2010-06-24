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

Account info samples.

@author: ilgar
"""
from ConfigParser import ConfigParser


def load_properties():
    properties = "client-local.properties"
    cfg = ConfigParser()
    cfg.read(properties)

    p = {}
    p['domain'] = cfg.get("domain", "name")
    p['hostname'] = cfg.get("domain", "host")
    p['domain_key'] = cfg.get("domain", "key")

    p['proxy_scheme'] = cfg.get("proxy", "scheme")
    p['proxy_hostname'] = cfg.get("proxy", "host")
    p['proxy_port'] = cfg.get("proxy", "port")
    p['proxy_username'] = cfg.get("proxy", "username")
    p['proxy_password'] = cfg.get("proxy", "password")

    p['username'] = cfg.get("auth", "username")
    p['account_name'] = '%s@%s' % (p['username'], p['domain'])
    p['password'] = cfg.get("auth", "password")

    return p
