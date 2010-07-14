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
from pyzimbra.base import ZObject


class AccountInfo(ZObject):
    """
    """
    # --------------------------------------------------------------- properties
    name = property(lambda self: self._name,
                    lambda self, v: setattr(self, '_name', v))
    soap_url = property(lambda self: self._soap_url,
                        lambda self, v: setattr(self, '_soap_url', v))
    public_url = property(lambda self: self._public_url,
                          lambda self, v: setattr(self, '_public_url', v))
    attrs = property(lambda self: self._attrs,
                          lambda self, v: setattr(self, '_attrs', v))  


    # -------------------------------------------------------------------- bound
    def __init__(self):
        ZObject.__init__(self)

        self.name = None
        self.soap_url = None
        self.public_url = None
        self.attrs = {}


    def __str__(self):
        return self.__unicode__()


    def __unicode__(self):
        return ('name: %s; soap_url: %s; public_url: %s; attrs: %s'
                % (self.name, self.soap_url, self.public_url, self.attrs))


    # ------------------------------------------------------------------ unbound
    def parse(self, res):
        """
        Parses xml structure.
        @param res: xml response from zimbra
        """
        self.name = res.name
        self.soap_url = res.soapURL
        self.public_url = res.publicURL
