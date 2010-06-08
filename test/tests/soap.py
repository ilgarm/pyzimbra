# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from base import BaseTest
from lxml import etree
from pyzimbra import zconstant, soap, sconstant
from pyzimbra.soap import wrap_soap_payload, unwrap_soap_payload, SoapException
import unittest


class SoapTest(BaseTest, unittest.TestCase):

    # ------------------------------------------------------------------ unbound
    def setUp(self):
        BaseTest.setUp(self)


    def tearDown(self):
        BaseTest.tearDown(self)


    # -------------------------------------------------------------------- tests
    def testEmptyHostname(self):
        self.assertRaises(SoapException, soap.soap_url, "")


    def testNotEmptyHostname(self):
        result = soap.soap_url("localhost")
        self.assertEqual("http://localhost/service/soap", result)


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

        res = etree.Element('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                      sconstant.AuthResponse),
                            nsmap=zconstant.NS_ZIMBRA_ACC_MAP)

        e = etree.SubElement(res, '%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                            sconstant.E_AUTH_TOKEN))
        e.text = 'token_abcdef'

        e = etree.SubElement(res, '%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                            sconstant.E_SESSION_ID),
                             attrib={sconstant.A_ID: '12345'})
        e.text = '12345'

        self.assertEqual('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                   sconstant.AuthResponse), res.tag)

        result = res.findtext('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                        sconstant.E_AUTH_TOKEN))
        self.assertEqual('token_abcdef', result)

        result = res.findtext('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                        sconstant.E_SESSION_ID))
        self.assertEqual('12345', result)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
