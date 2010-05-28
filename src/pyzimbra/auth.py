# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from pyzimbra import util, zutil, soap
import urllib2


class AuthException(Exception):
    """
    Authentication exception.
    """
    title = property(lambda self: self._title, 
                     lambda self, v: setattr(self, '_title', v))
    message = property(lambda self: self._message, 
                       lambda self, v: setattr(self, '_message', v))

    # -------------------------------------------------------------------- bound
    def __init__(self, message, title = None, show_traceback = False):
        Exception.__init__(self, message)

        self._message = message
        if title:
            self._title = title
        self.show_traceback = show_traceback

    def __unicode__(self):
        return unicode(self.message)


class AuthToken(object):
    """
    AuthToken holds current authentication token and sessions id.
    """
    token = property(lambda self: self._token,
                     lambda self, v: setattr(self, '_token', v))
    session_id = property(lambda self: self._session_id,
                          lambda self, v: setattr(self, '_session_id', v))


    def __init__(self):
        """
        Constructor
        """


class Authenticator(object):
    """
    Authenticator provides methods to authenticate using username/password 
    as a user or administrator or using domain key.
    """
    # --------------------------------------------------------------- properties
    hostname = property(lambda self: self._hostname,
                        lambda self, v: setattr(self, '_hostname', v))
    domain = property(lambda self: self._domain,
                      lambda self, v: setattr(self, '_domain', v))
    domain_key = property(lambda self: self._domain_key,
                          lambda self, v: setattr(self, '_domain_key', v))
    username = property(lambda self: self._username,
                        lambda self, v: setattr(self, '_username', v))
    password = property(lambda self: self._password,
                        lambda self, v: setattr(self, '_password', v))

    # -------------------------------------------------------------------- bound
    def __init__(self):
        """
        Constructor
        """

    # ------------------------------------------------------------------ unbound
    def authenticate(self, username, password):
        """
        Authenticates account.
        
        @param username: account name, can be local part or full email
        @param password: account password
        
        @raise AuthException: if authentication fails
        @return: AuthToken if authentication succeeded
        """
        if util.empty(username):
            raise AuthException('Empty username')

        if util.empty(password):
            raise AuthException('Empty password')

        url = zutil.soap_url(self.hostname)
        req = soap.prepare_auth_request(self.hostname,
                                        '%s@%s' % (username, self.domain),
                                        password)
        try:
            res = soap.send_request(url, req)
        except urllib2.HTTPError:
            raise AuthException('Authentication failed')

        token = AuthToken()
        token.token = "some token here"
        token.session_id = "some session id here"

        return token
