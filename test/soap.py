# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from lxml import etree
from pyzimbra.soap import wrap_soap_payload, unwrap_soap_payload
import unittest
from pyzimbra import zconstant
import lxml


class SoapTest(unittest.TestCase):

    # -------------------------------------------------------------------- tests
    def testWrapSimplePayload(self):

        req = etree.Element('test', nsmap=zconstant.NS_ZIMBRA_ACC_MAP)

        env = wrap_soap_payload(req)
        result = etree.tounicode(env)
        expected = "<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\"><soap:Header/><soap:Body><test xmlns=\"urn:zimbraAccount\"/></soap:Body></soap:Envelope>"
        self.assertEqual(expected, result)


    def testUnwrapSimplePayload(self):

        str = "<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\"><soap:Header/><soap:Body><test xmlns=\"urn:zimbraAccount\"/></soap:Body></soap:Envelope>"

        result = unwrap_soap_payload(str)
        self.assertEqual('{urn:zimbraAccount}test', result.tag)


    def testEtreeResponseParse(self):

        str = "<AuthResponse xmlns=\"urn:zimbraAccount\" xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\"><authToken>token_abcdef</authToken><lifetime>86400000</lifetime><sessionId id=\"12345\">12345</sessionId></AuthResponse>"
        res = lxml.etree.fromstring(str)

        self.assertEqual('{urn:zimbraAccount}AuthResponse', res.tag)

        result = res.findtext('{urn:zimbraAccount}authToken')
        self.assertEqual('token_abcdef', result)

        result = res.findtext('{urn:zimbraAccount}lifetime')
        self.assertEqual('86400000', result)

        result = res.findtext('{urn:zimbraAccount}sessionId')
        self.assertEqual('12345', result)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
