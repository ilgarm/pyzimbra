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

__version__ = '0.1'
USER_AGENT = "pyzimbra/%s" % __version__

SOAP_URL = '/service/soap'
SOAP_ADMIN_URL = '/service/admin/soap'

SOAP_DEFAULT_PREFIX = 'ns1'

NS_SOAP_URL = 'http://www.w3.org/2003/05/soap-envelope'
NS_SOAP_PREFIX = 'soap'
NS_SOAP_MAP = {NS_SOAP_PREFIX: NS_SOAP_URL}
NS_SOAP = '{%s}' % NS_SOAP_URL

NS_ZIMBRA_URL = 'urn:zimbra'
NS_ZIMBRA_MAP = {None: NS_ZIMBRA_URL}
NS_ZIMBRA = '{%s}' % NS_ZIMBRA_URL

NS_ZIMBRA_ACC_URL = 'urn:zimbraAccount'
NS_ZIMBRA_ACC_MAP = {None: NS_ZIMBRA_ACC_URL}
NS_ZIMBRA_ACC = '{%s}' % NS_ZIMBRA_ACC_URL

NS_ZIMBRA_ADMIN_URL = 'urn:zimbraAdmin'
NS_ZIMBRA_ACC_MAP = {None: NS_ZIMBRA_ADMIN_URL}
NS_ZIMBRA_ACC = '{%s}' % NS_ZIMBRA_ADMIN_URL
