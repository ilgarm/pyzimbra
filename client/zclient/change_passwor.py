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
################################################################################.

@author: ilgar
"""
from client.util import init_client
from test import pconstant
import time


@init_client
def run(p, zclient):

    zclient.change_password(p[pconstant.PASSWORD], p[pconstant.PASSWORD] + '_new')
    time.sleep(3)
    zclient.change_password(p[pconstant.PASSWORD] + '_new', p[pconstant.PASSWORD])


if __name__ == '__main__':
    run()
