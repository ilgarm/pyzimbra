# -*- coding: utf-8 -*-
"""
Zimbra client related methods and classes.

@author: ilgar
"""
import abc
import traceback


class ZimbraClientException(Exception):
    """
    Zimbra client exception.
    """
    # --------------------------------------------------------------- properties
    message = property(lambda self: self._message, 
                       lambda self, v: setattr(self, '_message', v))
    tracebacks = property(lambda self: self._tracebacks,
                          lambda self, v: setattr(self, '_tracebacks', v))

    # -------------------------------------------------------------------- bound
    def __init__(self, message, cause = None):
        Exception.__init__(self, message)

        self._message = message

        self.tracebacks = []
        if cause != None:
            if isinstance(cause, ZimbraClientException):
                self.tracebacks = cause.tracebacks
        list = traceback.format_exc().split('\n')[1:]
        self.tracebacks.insert(0, '\n'.join(list))


    def __str(self):
        return self.message


    def __unicode__(self):
        return unicode(self.message)


    # ------------------------------------------------------------------ unbound
    def print_trace(self):
        """
        Prints stack trace for current exceptions chain.
        """
        traceback.print_exc()
        for tb in self.tracebacks:
            print tb,
        print ''


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
