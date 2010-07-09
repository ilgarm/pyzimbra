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
from pyzimbra.soap_transport import SoapHttpTransport
from test.base import BaseTest
from test.mock.soap import MockTransport
import unittest
import urllib2


class SoapHttpTransportTest(BaseTest, unittest.TestCase):

    # ------------------------------------------------------------------ unbound
    def setUp(self):
        BaseTest.setUp(self)


    def tearDown(self):
        BaseTest.tearDown(self)


    # -------------------------------------------------------------------- tests
    def testInitSoapException(self):
        
        transport = SoapHttpTransport()

        result = transport.init_soap_exception(ValueError())
        self.assertEqual(None, result.code)
        self.assertEqual(None, result.trace)


    def testUnwrapSoapException(self):
        transport = SoapHttpTransport()
        transport.transport = MockTransport()

        str = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Header>
        <context xmlns="urn:zimbra"/>
        </soap:Header>
        <soap:Body>
        <soap:Fault>
        <soap:faultcode>soap:CODE</soap:faultcode>
        <soap:faultstring>MESSAGE</soap:faultstring>
        <soap:detail>
        <Error xmlns="urn:zimbra">
        <Code>CODE</Code>
        <Trace>TRACE</Trace>
        </Error>
        </soap:detail>
        </soap:Fault>
        </soap:Body>
        </soap:Envelope>
        """
        def read():
            return str

        exc = urllib2.HTTPError('url', '500', 'message', None, None)
        exc.read = read

        result = transport.init_soap_exception(exc)
        self.assertEqual('soap:CODE:MESSAGE', result.message)
        self.assertEqual('CODE', result.code)
        self.assertEqual('TRACE', result.trace)


if __name__ == "__main__":
#    import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
