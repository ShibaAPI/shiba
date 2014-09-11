#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class ShibaInit
# Shiba initialization class


from __future__ import unicode_literals

from shibaexceptions import *


class ShibaConnection(object):
    def __init__(self, login, pwd, domain="https://ws.priceminister.com"):
        """
        :param login: PriceMinister Seller login
        :param pwd: PriceMinister Seller Token
        (see more at https://developer.priceminister.com/blog/fr/documentation/identification-by-token)
        :param domain: give it the sandbox domain version of WebServices if you want to test this interface
        on a sandboxed version of PriceMinister
        """
        self.login = str(login)
        self.pwd = str(pwd)
        if len(domain) == 0:
            raise ShibaCallingError("Shiba init error : given domain is empty")
        self.domain = domain
        """URL generation relative dictionary, formatting URLs in methods from the given format, first '%s'
        is the action type, given as primary key"""
        self.actionsinfo = \
        {"producttypes": {"cat": "stock_ws", "version": "2011-11-29", "login": self.login, "pwd": self.pwd},
        "producttypetemplate": {"cat": "stock_ws", "version": "2013-05-14", "login": self.login, "pwd": self.pwd},
        "genericimportfile": {"cat": "stock_ws", "version": "2012-09-11", "login": self.login, "pwd": self.pwd},
        "genericimportreport": {"cat": "stock_ws", "version": "2011-11-29", "login": self.login, "pwd": self.pwd},
        "getavailableshippingtypes": {"cat": "sales_ws", "version": "2013-06-25", "login": self.login, "pwd": self.pwd},
        "export": {"cat": "stock_ws", "version": "2014-01-28", "login": self.login, "pwd": self.pwd},
        "listing": {"cat": "listing_ws", "version": "2014-01-28", "login": self.login, "pwd": self.pwd},
        "categorymap": {"cat": "categorymap_ws", "version": "2011-10-11", "login": self.login, "pwd": self.pwd},
        "getnewsales": {"cat": "sales_ws", "version": "2014-02-11", "login": self.login, "pwd": self.pwd},
        "acceptsale": {"cat": "sales_ws", "version": "2010-09-20", "login": self.login, "pwd": self.pwd},
        "refusesale": {"cat": "sales_ws", "version": "2010-09-20", "login": self.login, "pwd": self.pwd},
        "getcurrentsales": {"cat": "sales_ws", "version": "2014-02-11", "login": self.login, "pwd": self.pwd},
        "getbillinginformation": {"cat": "sales_ws", "version": "2011-03-29", "login": self.login, "pwd": self.pwd},
        "getshippinginformation": {"cat": "sales_ws", "version": "2014-02-11", "login": self.login, "pwd": self.pwd},
        "getitemtodolist": {"cat": "sales_ws", "version": "2011-09-01", "login": self.login, "pwd": self.pwd},
        "getiteminfos": {"cat": "sales_ws", "version": "2011-06-01", "login": self.login, "pwd": self.pwd},
        "cancelitem": {"cat": "sales_ws", "version": "2011-02-02", "login": self.login, "pwd": self.pwd},
        "contactusaboutitem": {"cat": "sales_ws", "version": "2011-09-01", "login": self.login, "pwd": self.pwd},
        "contactuseraboutitem": {"cat": "sales_ws", "version": "2011-02-02", "login": self.login, "pwd": self.pwd},
        "settrackingpackageinfos": {"cat": "sales_ws", "version": "2012-11-06", "login": self.login, "pwd": self.pwd},
        "confirmpreorder": {"cat": "sales_ws", "version": "2013-01-09", "login": self.login, "pwd": self.pwd},
        "getoperations": {"cat": "wallet_ws", "version": "2011-03-29", "login": self.login, "pwd": self.pwd},
        "getcompensationdetails": {"cat": "sales_ws", "version": "2011-03-29", "login": self.login, "pwd": self.pwd}}