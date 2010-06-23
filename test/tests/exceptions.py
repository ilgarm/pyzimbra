# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
from pyzimbra.base import ZimbraClientException


class TestException2(ZimbraClientException):
    def __init__(self, message, cause = None):
        ZimbraClientException.__init__(self, message, cause)

class TestException3(ZimbraClientException):
    def __init__(self, message, cause = None):
        ZimbraClientException.__init__(self, message, cause)

def m1():
    raise TypeError('exception 1')

def m2():
    try:
        m1()
    except Exception, e:
        raise TestException2('exception 2', e)

def m3():
    try:
        m2()
    except Exception, e:
        raise TestException3('exception 3', e)


if __name__ == "__main__":
    try:
        m3()
    except ZimbraClientException, e:
        e.print_trace()
