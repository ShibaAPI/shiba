# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class ShibaConnection(object):
    """The main Shiba class, standing as an initialization and mandatory for each submodules instancing.

        :param login: PriceMinister Seller login
        :param pwd: PriceMinister Seller Token \
        (see more at https://developer.priceminister.com/blog/fr/documentation/identification-by-token)
        :param sandbox: give it True if you want to test the API on a sandboxed version of PriceMinister.
        """

    def __init__(self, login, pwd, sandbox=False):
        self.login = str(login)
        self.pwd = str(pwd)
        self.domain = "https://ws.fr.shopping.rakuten.com" if sandbox is False else "https://ws.fr.shopping.rakuten.com"
        self.actionsinfo = {
            "producttypes": {"cat": "stock_ws", "version": "2015-06-30", "login": self.login, "pwd": self.pwd},
            "producttypetemplate": {"cat": "stock_ws", "version": "2017-10-04", "login": self.login, "pwd": self.pwd},
            "genericimportfile": {"cat": "stock_ws", "version": "2015-02-02", "login": self.login, "pwd": self.pwd},
            "genericimportreport": {"cat": "stock_ws", "version": "2017-02-10", "login": self.login, "pwd": self.pwd},
            "getavailableshippingtypes": {"cat": "sales_ws", "version": "2013-06-25", "login": self.login,
                                          "pwd": self.pwd},
            "export": {"cat": "stock_ws", "version": "2018-06-29", "login": self.login, "pwd": self.pwd},
            "listing": {"cat": "listing_ssl_ws", "version": "2018-06-28", "login": self.login, "pwd": self.pwd},
            "categorymap": {"cat": "categorymap_ws", "version": "2011-10-11", "login": self.login, "pwd": self.pwd},
            "getnewsales": {"cat": "sales_ws", "version": "2017-08-07", "login": self.login, "pwd": self.pwd},
            "acceptsale": {"cat": "sales_ws", "version": "2010-09-20", "login": self.login, "pwd": self.pwd},
            "refusesale": {"cat": "sales_ws", "version": "2010-09-20", "login": self.login, "pwd": self.pwd},
            "getcurrentsales": {"cat": "sales_ws", "version": "2017-08-07", "login": self.login, "pwd": self.pwd},
            "getbillinginformation": {"cat": "sales_ws", "version": "2016-03-16", "login": self.login,
                                      "pwd": self.pwd},
            "getshippinginformation": {"cat": "sales_ws", "version": "2017-09-12", "login": self.login,
                                       "pwd": self.pwd},
            "getitemtodolist": {"cat": "sales_ws", "version": "2011-09-01", "login": self.login, "pwd": self.pwd},
            "getiteminfos": {"cat": "sales_ws", "version": "2017-08-07", "login": self.login, "pwd": self.pwd},
            "cancelitem": {"cat": "sales_ws", "version": "2011-02-02", "login": self.login, "pwd": self.pwd},
            "contactusaboutitem": {"cat": "sales_ws", "version": "2011-09-01", "login": self.login, "pwd": self.pwd},
            "contactuseraboutitem": {"cat": "sales_ws", "version": "2011-02-02", "login": self.login, "pwd": self.pwd},
            "settrackingpackageinfos": {"cat": "sales_ws", "version": "2016-03-16", "login": self.login,
                                        "pwd": self.pwd},
            "confirmpreorder": {"cat": "sales_ws", "version": "2013-01-09", "login": self.login, "pwd": self.pwd},
            "getoperations": {"cat": "wallet_ws", "version": "2011-03-29", "login": self.login, "pwd": self.pwd},
            "getcompensationdetails": {"cat": "sales_ws", "version": "2011-03-29", "login": self.login,
                                       "pwd": self.pwd}
        }
