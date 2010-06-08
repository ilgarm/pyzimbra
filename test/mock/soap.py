# -*- coding: utf-8 -*-
"""
Soap related mockups.

@author: ilgar
"""
from pyzimbra.base import ZimbraClientTransport
import urllib2
from mock import responses
from util import load_test_properties


class MockTransport(ZimbraClientTransport):
    """
    Mocked transport.
    """
    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        ZimbraClientTransport.__init__(self)

        load_test_properties(self)


    # ------------------------------------------------------------------ unbound
    def invoke(self, req):
        return responses.get_response(req, self)


class MockFailingTransport(ZimbraClientTransport):
    """
    Mocked failing transport.
    """
    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        ZimbraClientTransport.__init__(self)

        load_test_properties(self)


    # ------------------------------------------------------------------ unbound
    def invoke(self, req):
        raise urllib2.HTTPError('', '500', 'Mocked Error', None, None)
