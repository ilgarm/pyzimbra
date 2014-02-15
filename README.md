# Zimbra Python Client (pyzimbra)

### About

This library aimed to help those who want to talk to zimbra instance from python.
Current version is 0.1. Released under [LGPL](http://www.gnu.org/licenses/lgpl.html) license.

### Features

There is not much, actually.

What is possible at the moment:
 * authentication to zimbra using account name and password
 * pre-authentication to zimbra using domain key
 * administrative login to zimbra
 * execute any method via soap by preparing xml request
 * get back proper exception message and code from zimbra
 * use library behind proxy

What is missing and coming in the future:
 * zimbra client api: set of python classes to use instead of dealing with xml directly

### Prerequisites

Install [SOAPpy](http://pywebsvcs.sourceforge.net/)

### Installation

    #!sh
    tar xfz pyzimbra-0.1.tar.gz
    cd pyzimbra-0.1
    python setup.py install

### How to use

Several examples are available on repository under client/sample directory.
Please, note that client and test directories from the source tree are not part of binary distribution.

### Contacts

For any purpose, I am available at the following address: [project name]@lab.az
