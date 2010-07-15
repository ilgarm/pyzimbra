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
from pyzimbra import soap
from pyzimbra.z.client import ZimbraClient
from test import pconstant
import logging
import sys


def load_properties():
    properties = "../client-local.properties"
    cfg = ConfigParser()
    cfg.read(properties)

    p = {}
    p[pconstant.ADMIN_HOSTNAME] = cfg.get(pconstant.ADMIN, pconstant.HOST)
    p[pconstant.ADMIN_ACCOUNT_NAME] = cfg.get(pconstant.ADMIN, pconstant.USERNAME)
    p[pconstant.ADMIN_PASSWORD] = cfg.get(pconstant.ADMIN, pconstant.PASSWORD)

    p[pconstant.DOMAIN] = cfg.get(pconstant.DOMAIN, pconstant.NAME)
    p[pconstant.HOSTNAME] = cfg.get(pconstant.DOMAIN, pconstant.HOST)
    p[pconstant.DOMAINS] = {p[pconstant.DOMAIN]:
                            cfg.get(pconstant.DOMAIN, pconstant.KEY)}

    p[pconstant.PROXY_SCHEME] = cfg.get(pconstant.PROXY, pconstant.SCHEME)
    p[pconstant.PROXY_HOSTNAME] = cfg.get(pconstant.PROXY, pconstant.HOST)
    p[pconstant.PROXY_PORT] = cfg.get(pconstant.PROXY, pconstant.PORT)
    p[pconstant.PROXY_USERNAME] = cfg.get(pconstant.PROXY, pconstant.USERNAME)
    p[pconstant.PROXY_PASSWORD] = cfg.get(pconstant.PROXY, pconstant.PASSWORD)

    p[pconstant.USERNAME] = cfg.get(pconstant.AUTH, pconstant.USERNAME)
    p[pconstant.ACCOUNT_NAME] = '%s@%s' % (p[pconstant.USERNAME], p[pconstant.DOMAIN])
    p[pconstant.PASSWORD] = cfg.get(pconstant.AUTH, pconstant.PASSWORD)

    return p


def init_client(f):
    def call():
        logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)

        p = load_properties()

        zclient = ZimbraClient(soap.soap_url(p[pconstant.HOSTNAME]))
        zclient.authenticate(p[pconstant.ACCOUNT_NAME], p[pconstant.PASSWORD])

        return f(p, zclient)
    return call


def init_proxied_client(f):
    def call():
        logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)

        p = load_properties()

        proxy_url = soap.proxy_url(p[pconstant.PROXY_HOSTNAME],
                                   p[pconstant.PROXY_USERNAME],
                                   p[pconstant.PROXY_PASSWORD],
                                   p[pconstant.PROXY_PORT],
                                   p[pconstant.PROXY_SCHEME])
    
        zclient = ZimbraClient(soap.soap_url(p[pconstant.HOSTNAME]),
                               proxy_url=proxy_url)
        zclient.authenticate(p[pconstant.ACCOUNT_NAME], p[pconstant.PASSWORD])

        return f(p, zclient)
    return call
