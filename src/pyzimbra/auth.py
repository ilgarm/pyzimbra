# -*- coding: utf-8 -*-
"""
Authentication related methods and classes.

@author: ilgar
"""
from pyzimbra import util
from pyzimbra.base import ZimbraClientTransport, ZimbraClientException
import abc


class AuthException(ZimbraClientException):
    """
    Authentication exception.
    """
    # -------------------------------------------------------------------- bound
    def __init__(self, message, cause = None):
        ZimbraClientException.__init__(self, message, cause)


class AuthToken(object):
    """
    AuthToken holds current authentication token and sessions id.
    """
    # --------------------------------------------------------------- properties
    account_name = property(lambda self: self._account_name,
                            lambda self, v: setattr(self, '_account_name', v))
    token = property(lambda self: self._token,
                     lambda self, v: setattr(self, '_token', v))
    session_id = property(lambda self: self._session_id,
                          lambda self, v: setattr(self, '_session_id', v))


    # -------------------------------------------------------------------- bound
    def __init__(self):
        self.account_name = None
        self.token = None
        self.session_id = None


class Authenticator(object):
    """
    Authenticator provides methods to authenticate using username/password 
    as a user or administrator or using domain key.
    """
    __metaclass__ = abc.ABCMeta

    # --------------------------------------------------------------- properties

    # -------------------------------------------------------------------- bound
    def __init__(self):
        pass

    # ------------------------------------------------------------------ unbound
    @abc.abstractmethod
    def authenticate(self, transport, account_name, password):
        """
        Authenticates account.
        @param transport: transport to use for method calls
        @param account_name: account name
        @param password: account password
        @return: AuthToken if authentication succeeded
        @raise AuthException: if authentication fails
        """
        if not isinstance(transport, ZimbraClientTransport):
            raise ZimbraClientException('Invalid transport')

        if util.empty(account_name):
            raise AuthException('Empty account name')

        if util.empty(password):
            raise AuthException('Empty password')
