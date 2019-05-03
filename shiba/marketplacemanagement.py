# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .shibaconnection import ShibaConnection
from .shibatools import inf_constructor, url_constructor, retrieve_obj_from_url
from .compat import basestring


class MarketplaceManagement(object):
    """ Marketplace informations retrieving, such as product lists and category mapping"""

    def __init__(self, connection):
        if not isinstance(connection, ShibaConnection):
            raise ValueError("expecting a ShibaConnection instance, got '%s'" % type(connection))
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
        if not isinstance(refs, basestring) and not isinstance(refs, list):
            raise ValueError("expected string or list for 'refs', got '%s'" % type(refs))

        if not isinstance(productids, basestring) and not isinstance(productids, list):
            raise ValueError("expected string or list for 'productids', got '%s'" % type(productids))

        if isinstance(refs, list):
            refs = ','.join(refs)
        if isinstance(productids, list):
            productids = ','.join(productids)
        if kw != u'':
            # TODO: and ???
            pass
        inf = inf_constructor(self.connection, "listing", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def get_category_map(self):
        """Lists items categories from the PriceMinister platform"""
        inf = inf_constructor(self.connection, "categorymap", **locals())
        url = url_constructor(self.connection, inf, domain="https://ws.fr.shopping.rakuten.com")
        obj = retrieve_obj_from_url(url)
        return obj
