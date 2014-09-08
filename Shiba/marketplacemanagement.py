#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class MarketplaceManagement


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
        """Prints a list from given parameters.

        :param scope: None (classic results), "PRICING" (classic results plus 10 best announces)
        or "LIMITED" (search in categories in which rapid put on sale is possible through WS)
        :param kw: Research keyword
        :param nav: Navigation category (url friendly ones, can be found on PriceMinister categories' URLs)
        :param refs: EAN, or ISBN, as a string, each value separated by a coma ','.
        :param productids: Same as refs but as products ID.
        :param nbproductsperpage: Products per page, default is 20.
        :param pagenumber: Page number, default is 1.
        """
        if type(refs) is not list or str or type(productids) is not list or str:
            raise ShibaCallingError("Shiba code error : expected list or str as refs and/or productids parameters")
        inf = ShibaTools.inf_constructor(self.connection, "listing", **locals())
        url = ShibaTools.url_constructor(self.connection, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def get_category_map(self):
        """Lists items categories from the PriceMinister platform"""
        inf = ShibaTools.inf_constructor(self.connection, "categorymap", **locals())
        url = ShibaTools.url_constructor(self.connection, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj