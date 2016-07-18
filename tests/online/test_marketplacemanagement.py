#!/usr/bin/env python
from __future__ import unicode_literals

from shiba.marketplacemanagement import MarketplaceManagement
from shiba.shibaexceptions import *


def test_get_product_list(connection):
    """testing get_product_list methods with different queries, with some invalid ones as well"""
    marketplace_management = MarketplaceManagement(connection)
    try:
        obj = marketplace_management.get_product_list()
    except ShibaParameterError:
        pass
    obj = marketplace_management.get_product_list(kw="livre")
    assert "listingresult" in obj.content.tag
    try:
        obj = marketplace_management.get_product_list(nbproductsperpage=-15, kw="livre")
    except ShibaParameterError:
        pass
    obj = marketplace_management.get_product_list(kw="informatique", scope="PRICING")
    assert "listingresult" in obj.content.tag


def test_get_category_map(connection):
    """get_category_map regular test"""
    marketplace_management = MarketplaceManagement(connection)
    obj = marketplace_management.get_category_map()
    assert "categorymap" in obj.content.tag
