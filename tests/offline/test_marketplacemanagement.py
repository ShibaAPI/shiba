#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class MarketplaceManagementTest
# Testing MarketplaceManagement Class methods
# https://developer.priceminister.com/blog/fr/documentation/product-data


from __future__ import unicode_literals

from shiba.marketplacemanagement import MarketplaceManagement
from shiba.shibaconnection import ShibaConnection
from shiba.shibaexceptions import *

import unittest

import os
import mock


def mock_get_product_list(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_getproductlist.xml'))
    return datas


def mock_get_category_map(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_getcategorymap.xml'))
    return datas


class MarketplaceManagementTest(unittest.TestCase):

    def setUp(self):
        self.init = MarketplaceManagement(ShibaConnection("test", "test" "https://ws.sandbox.priceminister.com"))

    @mock.patch('urllib2.urlopen', side_effect=mock_get_product_list)
    def test_get_product_list(self, urlopen):
        """testing get_product_list methods with different queries, with some invalid ones as well"""
        try:
            obj = self.init.get_product_list()
        except ShibaParameterError:
            pass
        obj = self.init.get_product_list(kw="livre")
        self.assertIn("listingresult", obj.content.tag)
        try:
            obj = self.init.get_product_list(nbproductsperpage=-15, kw="livre")
        except ShibaParameterError:
            pass
        obj = self.init.get_product_list(kw="informatique", scope="PRICING")
        self.assertIn("listingresult", obj.content.tag)

    @mock.patch('urllib2.urlopen', side_effect=mock_get_category_map)
    def test_get_category_map(self, urlopen):
        """get_category_map regular test"""
        obj = self.init.get_category_map()
        self.assertIn("categorymap", obj.content.tag)
