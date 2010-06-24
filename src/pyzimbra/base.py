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

Zimbra client related methods and classes.

@author: ilgar
"""
import abc
import traceback


class ZimbraClientException(Exception):
    """
    Zimbra client exception.
    """
    # --------------------------------------------------------------- properties
    message = property(lambda self: self._message, 
                       lambda self, v: setattr(self, '_message', v))
    tracebacks = property(lambda self: self._tracebacks,
                          lambda self, v: setattr(self, '_tracebacks', v))

    # -------------------------------------------------------------------- bound
    def __init__(self, message, cause = None):
        Exception.__init__(self, message)

        self._message = message
        self.__cause__ = cause

        self.tracebacks = []
        if cause != None:
            if isinstance(cause, ZimbraClientException):
                self.tracebacks = cause.tracebacks
        list = traceback.format_exc().split('\n')[1:]
        self.tracebacks.insert(0, '\n'.join(list))


    def __unicode__(self):
        return self.message


    # ------------------------------------------------------------------ unbound
    def print_trace(self):
        """
        Prints stack trace for current exceptions chain.
        """
        traceback.print_exc()
        for tb in self.tracebacks:
            print tb,
        print ''


class ZimbraClientTransport(object):
    """
    Transport base class. 
    """
    __metaclass__ = abc.ABCMeta

    # --------------------------------------------------------------- properties
    url = property(lambda self: self._url,
                   lambda self, v: setattr(self, '_url', v))
    proxy_url = property(lambda self: self._proxy_url,
                         lambda self, v: setattr(self, '_proxy_url', v))

    # -------------------------------------------------------------------- bound
    def __init__(self):
        self.url = None
        self.proxy_url = None

    # ------------------------------------------------------------------ unbound
    @abc.abstractmethod
    def invoke(self, req, auth_token):
        """
        Invokes zimbra request.
        @param req: request to invoke
        @param auth_token: authentication token to use for session
        @return: zimbra response
        """
