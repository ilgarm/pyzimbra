# -*- coding: utf-8 -*-
"""
@author: ilgar
"""

SOAP_URL = '/service/soap'

USER_AGENT = 'ZimbraPython/1.0 +http://localhost/'

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
