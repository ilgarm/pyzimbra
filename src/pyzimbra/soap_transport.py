# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from pyzimbra.soap import wrap_soap_payload, unwrap_soap_payload
import gzip
import io
import urllib2
from pyzimbra import zconstant


def send_request(url, req):
    """
    Sends request to zimbra endpoint and extracts payload
    """
    env = wrap_soap_payload(req)

    encoded = env
    headers = { 'User-Agent' : zconstant.USER_AGENT,
               'Accept-encoding' : 'gzip' }
    request = urllib2.Request(url, encoded, headers)
    response = urllib2.urlopen(request)
    data = response.read()

    if hasattr(response, 'headers'):
        if response.headers.get('content-encoding', '') == 'gzip':
            data = gzip.GzipFile(fileobj=io.StringIO(data)).read()

    return unwrap_soap_payload(data)
