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
from pyzimbra import util
from test.base import BaseTest
import unittest


class UtilTest(BaseTest, unittest.TestCase):

    # ------------------------------------------------------------------ unbound
    def setUp(self):
        BaseTest.setUp(self)


    def tearDown(self):
        BaseTest.tearDown(self)


    # -------------------------------------------------------------------- tests
    def testEmptyNone(self):
        result = util.empty(None)
        self.assertTrue(result)


    def testEmptyString(self):
        result = util.empty("")
        self.assertTrue(result)

        result = util.empty("some string")
        self.assertFalse(result)


    def testGetDomain(self):
        result = util.get_domain('noemail')
        self.assertEquals(None, result)

        result = util.get_domain('local@')
        self.assertEquals(None, result)

        result = util.get_domain('@domain')
        self.assertEquals('domain', result)

        result = util.get_domain('local@domain')
        self.assertEquals('domain', result)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
