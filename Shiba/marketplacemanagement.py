#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class MarketplaceManagement


from shibainit import ShibaInit
from shibatools import ShibaTools


class MarketplaceManagement(ShibaInit):
    """ Marketplace informations retrieving, such as product lists and category mapping"""

    def __init__(self, login, pwd, domain="https://ws.priceminister.com/"):
        super(MarketplaceManagement, self).__init__(login, pwd, domain)

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
        assert(type(refs) is not list or str or type(productids) is not list or str,
               "error : bad type given as refs or productids")
        inf = ShibaTools.inf_constructor(ShibaInit, "listing", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def get_category_map(self):
        inf = ShibaTools.inf_constructor(ShibaInit, "categorymap", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj