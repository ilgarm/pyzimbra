# -*- coding: utf-8 -*-
"""
Zimbra client related methods and classes.

@author: ilgar
"""
import abc


class ZimbraClientException(Exception):
    """
    Zimbra client exception.
    """
    # --------------------------------------------------------------- properties
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


class ZimbraClientTransport(object):
    """
    Transport base class. 
    """
    __metaclass__ = abc.ABCMeta

    # --------------------------------------------------------------- properties
    url = property(lambda self: self._url,
                   lambda self, v: setattr(self, '_url', v))
    proxy_url = property(lambda self: self._proxy_url,
                         lambda self, v: setattr(self, '_proxy_url', v))

    # -------------------------------------------------------------------- bound
    def __init__(self):
        self.url = None
        self.proxy_url = None

    # ------------------------------------------------------------------ unbound
    @abc.abstractmethod
    def invoke(self, req, auth_token):
        """
        Invokes zimbra request.
        @param req: request to invoke
        @param auth_token: authentication token to use for session
        @return: zimbra response
        """
