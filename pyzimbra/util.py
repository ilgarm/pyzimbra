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
import re


def empty(val):
    """
    Checks if value is empty.
    All unknown data types considered as empty values.
    @return: bool
    """
    if val == None:
        return True

    if isinstance(val,str) and len(val) > 0:
        return False

    return True


def get_domain(email):
    """
    Returns domain part of the email or None if invalid email format.
    @param email: email
    @return: str
    """
    match = re.search('^[^@]*?@([^@]+?)$', email)

    if match == None:
        return None

    return match.group(1)
