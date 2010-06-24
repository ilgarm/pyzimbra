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


#class SmartRedirectHandler(urllib2.HTTPRedirectHandler):
#    def http_error_301(self, req, fp, code, msg, headers):
#        result = urllib2.HTTPRedirectHandler.http_error_301(
#            self, req, fp, code, msg, headers)
#        result.status = code
#        return result
#
#    def http_error_302(self, req, fp, code, msg, headers):
#        result = urllib2.HTTPRedirectHandler.http_error_302(
#            self, req, fp, code, msg, headers)
#        result.status = code
#        return result
#
#class DefaultErrorHandler(urllib2.HTTPDefaultErrorHandler):
#    def http_error_default(self, req, fp, code, msg, headers):
#        result = urllib2.HTTPError(
#            req.get_full_url(), code, msg, headers, fp)
#        result.status = code
#        return result


def empty(val):
    """
    Checks if value is empty.
    All unknown data types considered as empty values.
    @return: bool
    """
    if val == None:
        return True

    # TODO: add emptiness checks for commonly used types
    if isinstance(val,str) and len(val) > 0:
        return False

    return True
