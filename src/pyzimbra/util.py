# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
import urllib2


class SmartRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(
            self, req, fp, code, msg, headers)
        result.status = code
        return result

    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_302(
            self, req, fp, code, msg, headers)
        result.status = code
        return result

class DefaultErrorHandler(urllib2.HTTPDefaultErrorHandler):
    def http_error_default(self, req, fp, code, msg, headers):
        result = urllib2.HTTPError(
            req.get_full_url(), code, msg, headers, fp)
        result.status = code
        return result


def empty(val):
    """
    Checks if value is empty.
    All unknown data types considered as empty values.
    @return: bool
    """
    if val == None:
        return True

    # TODO: add emptiness checks for commonly used types
    if isinstance(val,str) and len(val) > 0:
        return False

    return True
