# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from util import load_test_properties


class BaseTest(object):

    # --------------------------------------------------------------- properties
    domain = property(lambda self: self._domain,
                      lambda self, v: setattr(self, '_domain', v))
    hostname = property(lambda self: self._hostname,
                        lambda self, v: setattr(self, '_hostname', v))
    domain_key = property(lambda self: self._domain_key,
                          lambda self, v: setattr(self, '_domain_key', v))
    
    username = property(lambda self: self._username,
                        lambda self, v: setattr(self, '_username', v))
    account_name = property(lambda self: self._account_name,
                            lambda self, v: setattr(self, '_account_name', v))
    password = property(lambda self: self._password,
                        lambda self, v: setattr(self, '_password', v))
    token = property(lambda self: self._token,
                     lambda self, v: setattr(self, '_token', v))
    session_id = property(lambda self: self._session_id,
                          lambda self, v: setattr(self, '_session_id', v))


    # ------------------------------------------------------------------ unbound
    def setUp(self):
        load_test_properties(self)


    def tearDown(self):
        pass
