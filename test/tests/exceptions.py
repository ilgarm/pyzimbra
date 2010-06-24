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
from pyzimbra.base import ZimbraClientException


class TestException2(ZimbraClientException):
    def __init__(self, message, cause = None):
        ZimbraClientException.__init__(self, message, cause)

class TestException3(ZimbraClientException):
    def __init__(self, message, cause = None):
        ZimbraClientException.__init__(self, message, cause)

def m1():
    raise TypeError('exception 1')

def m2():
    try:
        m1()
    except Exception, e:
        raise TestException2('exception 2', e)

def m3():
    try:
        m2()
    except Exception, e:
        raise TestException3('exception 3', e)


if __name__ == "__main__":
    try:
        m3()
    except ZimbraClientException, e:
        e.print_trace()
