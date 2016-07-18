# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from shiba.marketplacemanagement import MarketplaceManagement
from shiba.shibaconnection import ShibaConnection

# from shiba.shibaexceptions import ShibaParameterError
# from . import assert_raises
from . import make_requests_get_mock


def test_get_product_list(monkeypatch):
    """testing get_product_list methods with different queries, with some invalid ones as well"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_getproductlist.xml'))

    shiba_connection = ShibaConnection("test", "test" "https://ws.sandbox.priceminister.com")
    marketplace_management = MarketplaceManagement(shiba_connection)

    # TODO: to remove ?
    # with assert_raises(ShibaParameterError):
    #     marketplace_management.get_product_list()

    product_list = marketplace_management.get_product_list(kw="livre")
    assert "listingresult" in product_list.content.tag

    # TODO: to remove ?
    # with assert_raises(ShibaParameterError):
    #     marketplace_management.get_product_list(nbproductsperpage=-15, kw="livre")

    product_list = marketplace_management.get_product_list(kw="informatique", scope="PRICING")
    assert "listingresult" in product_list.content.tag


def test_get_category_map(monkeypatch):
    """get_category_map regular test"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_getcategorymap.xml'))
    shiba_connection = ShibaConnection("test", "test" "https://ws.sandbox.priceminister.com")
    marketplace_management = MarketplaceManagement(shiba_connection)

    obj = marketplace_management.get_category_map()
    assert "categorymap" in obj.content.tag
