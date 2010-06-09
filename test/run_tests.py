# -*- coding: utf-8 -*-
"""
Test related methods and classes.

@author: ilgar
"""
from tests.auth import AuthTest
from tests.soap import SoapTest
from tests.soap_auth import SoapAuthTest
from tests.soap_transport import SoapTransportTest
from tests.util import UtilTest
from tests.zclient import ZimbraClientTest
import unittest


if __name__ == '__main__':
    unittest.TestSuite().main()
