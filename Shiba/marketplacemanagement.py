#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class MarketplaceManagement


from __future__ import unicode_literals

from shibaconnection import ShibaConnection
from shibatools import ShibaTools
from shibaexceptions import *


class MarketplaceManagement(object):
    """ Marketplace informations retrieving, such as product lists and category mapping"""

    def __init__(self, connection):
        if isinstance(connection, ShibaConnection) is False:
            raise ShibaCallingError("Shiba subclass init error : expecting a ShibaConnection instance")
        self.connection = connection

    def get_product_list(self, scope="", kw="", nav="", refs="", productids="", nbproductsperpage="", pagenumber=""):
        """Prints a search list result from given parameters.

        :param scope: none (classic results), "PRICING" (classic results plus 10 best announces)
            or "LIMITED" (search in categories in which rapid put on sale is possible through WS)
        :param kw: research keyword
        :param nav: navigation category (url friendly ones, can be found on PriceMinister categories' URLs)
        :param refs: EAN, or ISBN, as a string, each value separated by a coma ','.
        :param productids: same as refs but as products ID.
        :param nbproductsperpage: products per page, default is 20.
        :param pagenumber: page number, default is 1.
        """
        if (type(refs) is not list and type(refs) is not str and type(refs) is not unicode) or \
                (type(productids) is not list and type(productids) is not str and type(productids) is not unicode):
            raise ShibaCallingError \
            ("Shiba code error : expected list or str/unicode as refs and/or productids parameters"
                ", got " + unicode(type(refs)) + " as refs and " + unicode(type(productids))
                + " as productids instead.")
        if type(refs) is list:
            refs = ','.join(refs)
        if type(productids) is list:
            productids = ','.join(productids)
        inf = ShibaTools.inf_constructor(self.connection, "listing", **locals())
        url = ShibaTools.url_constructor(self.connection, inf, domain="http://ws.priceminister.com")
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def get_category_map(self):
        """Lists items categories from the PriceMinister platform"""
        inf = ShibaTools.inf_constructor(self.connection, "categorymap", **locals())
        url = ShibaTools.url_constructor(self.connection, inf, domain="http://ws.priceminister.com")
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj