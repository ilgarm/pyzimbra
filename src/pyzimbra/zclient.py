# -*- coding: utf-8 -*-
"""
Zimbra client related methods and classes.

@author: ilgar
"""
from pyzimbra.auth import AuthException
from pyzimbra.base import ZimbraClientException


class ZimbraClient(object):
    """
    Zimbra client main class.
    """
    # --------------------------------------------------------------- properties
    auth_token = property(lambda self: self._auth_token,
                          None)
    transport = property(lambda self: self._transport,
                         lambda self, v: setattr(self, '_transport', v))

    # -------------------------------------------------------------------- bound
    def __init__(self):
        self._auth_token = None
        self.transport = None

    # ------------------------------------------------------------------ unbound
    def authenticate(self, authenticator, account_name, password):
        """
        Authenticates zimbra account.
        @param authenticator: authenticator to use
        @param account_name: account email address
        @param password: account password
        @raise AuthException: if authentication fails
        @raise SoapException: if soap communication fails
        """
        if self.transport == None:
            raise ZimbraClientException('Invalid transport')

        self._auth_token = authenticator.authenticate(self.transport,
                                                      account_name, password)


    def invoke(self, req, auth_token=None):
        """
        Invokes zimbra method using established authentication session.
        @param req: zimbra request
        @param auth_token: alternative authentication session,
          if not provided existing one will be used 
        @return: zimbra response
        @raise AuthException: if authentication fails
        @raise SoapException: if soap communication fails
        @raise ZimbraClientException: wrapped server exception
        """
        if self.auth_token == None and auth_token == None:
            raise AuthException('Unable to invoke zimbra method')

        if req == None:
            raise ZimbraClientException('Invalid request')

        token = auth_token if auth_token != None else self._auth_token
        return self.transport.invoke(req, token)
