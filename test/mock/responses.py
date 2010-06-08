# -*- coding: utf-8 -*-
"""
Zimbra request and response mocked values.

@author: ilgar
"""
from lxml import etree
from pyzimbra import sconstant, zconstant


def get_response(req, test):

    if req.tag == sconstant.AuthRequest:
        return AuthResponse(req, test)

    return None


def AuthResponse(req, test):

    res = etree.Element('%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                  sconstant.AuthResponse),
                        nsmap=zconstant.NS_ZIMBRA_ACC_MAP)

    e = etree.SubElement(res, '%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                        sconstant.E_AUTH_TOKEN))
    e.text = test.token

    e = etree.SubElement(res, '%s%s' % (zconstant.NS_ZIMBRA_ACC,
                                        sconstant.E_SESSION_ID),
                         attrib={sconstant.A_ID: test.session_id})
    e.text = test.session_id

    return res


def GetInfoResponse(req, test):
    pass


#
#<GetInfoRequest [sections="mbox,prefs,attrs,zimlets,props,idents,sigs,dsrcs,children"]>
#</GetInfoRequest>
#
#<GetInfoResponse>
#   <version>{version}</version>
#   <id>{account-id}</id>
#   <name>{account-name}</name>
#   <lifetime>...</lifetime>   
#   [<rest>{account-base-REST-url}</rest>
#    <used>{used}</used>
#    <prevSession>{previous-SOAP-session}</prevSession>
#    <accessed>{last-SOAP-access}</accessed>
#    <recent>{recent-messages}</recent>
#   ]
#   <cos name="cos-name" id="cos-id"/>
#   <attrs>
#    <attr name="{name}">{value}</a>
#     ...
#    <attr name="{name}">{value}</a>
#   </attrs>
#   <prefs>
#     <pref name="{name}">{value}</pref>
#     ...
#     <pref name="{name}">{value}</pref>
#   </prefs>
#   <props>
#     <prop zimlet="{zimlet-name}" name="{name}">{value}</prop>
#     ...
#     <prop zimlet="{zimlet-name}" name="{name}">{value}</prop>
#   </props>
#   <zimlets>
#     <zimlet>
#       <zimletContext baseUrl="..."/>
#       <zimlet>...</zimlet>
#       <zimletConfig>...</zimletConfig>
#     </zimlet>
#     ...
#   </zimlets>
#   <mailURL>{mail-url}</mailURL>+
#   <publicURL>{account-base-public-url}</publicURL>
#   <identities>
#     <identity name={identity-name} id="...">
#       <a name="{name}">{value}</a>
#       ...
#       <a name="{name}">{value}</a>
#     </identity>*
#   </identities>
#   <signatures>
#     <signature name={signature-name} id="...">
#       <a name="{name}">{value}</a>
#       ...
#       <a name="{name}">{value}</a>
#     </signature>*
#   </signatures>
#   <dataSources>
#     <pop3 id="{id}" name="My POP3 Account" isEnabled="0|1" host="pop3.myisp.com" port="110"
#        username="mylogin" l="{folder-id}" [pollingInterval="10m"]/>
#     ...
#   </dataSources>*
#   <childAccounts>
#     <childAccount name="{child-account-name}" visible="0|1" id="{child-account-id}">
#         <attrs>
#            <attr name="{name}">{value}</a>*
#         </attrs>
#     </childAccount>*
#   </childAccounts>
#   [<license status="inGracePeriod|bad"/>]
#</GetInfoResponse>