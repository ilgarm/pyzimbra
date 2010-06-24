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

Zimbra request and response mocked values.

@author: ilgar
"""
from lxml import etree
from pyzimbra import sconstant, zconstant


def get_response(req, auth_token):

    if req.tag == sconstant.AuthRequest:
        return AuthResponse(req, auth_token)

    if req.tag == sconstant.GetInfoRequest:
        return GetInfoResponse(req, auth_token)

    return None


def AuthResponse(req, auth_token):

    res = etree.Element('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                  sconstant.AuthResponse),
                        nsmap=zconstant.NS_ZIMBRA_ACC_MAP)

    e = etree.SubElement(res, '%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                        sconstant.E_AUTH_TOKEN))
    e.text = auth_token.token

    e = etree.SubElement(res, '%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                        sconstant.E_SESSION_ID),
                         attrib={sconstant.A_ID: auth_token.session_id})
    e.text = auth_token.session_id

    return res


def GetInfoResponse(req, auth_token):
    res = etree.Element('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                  sconstant.GetInfoResponse),
                        nsmap=zconstant.NS_ZIMBRA_ACC_MAP)

    e = etree.SubElement(res, '%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                        sconstant.E_NAME))
    e.text = auth_token.account_name

    return res
