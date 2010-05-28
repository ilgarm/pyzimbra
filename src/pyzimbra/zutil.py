# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from pyzimbra import zconstant, util


class ZClientException(Exception):
    """
    Zimbra client exception.
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


def soap_url(hostname):
    """
    @raise ZClientException: 
    @return: absolute zimbra soap endpoint url
    """
    if util.empty(hostname):
            raise ZClientException('Empty hostname')

    return 'http://%s%s' % (hostname, zconstant.SOAP_URL)

