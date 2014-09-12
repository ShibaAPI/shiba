#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class MarketplaceManagementTest
# Testing MarketplaceManagement Class methods
# https://developer.priceminister.com/blog/fr/documentation/product-data


from __future__ import unicode_literals

from Shiba.marketplacemanagement import MarketplaceManagement
from Shiba.shibaconnection import ShibaConnection
from Shiba.shibaexceptions import *

import unittest

import ConfigParser
import os

class MarketplaceManagementTest(unittest.TestCase):

    def setUp(self):
        settings = ConfigParser.ConfigParser()
        try:
            settings.read(os.path.dirname(os.path.realpath(__file__)) + "/Assets/nosetests.cfg")
        except:
            raise ShibaCallingError("error : can't read login ID from the nosetests.cfg file")
        try:
            login = settings.get(str("NoseConfig"), "login")
            pwd = settings.get(str("NoseConfig"), "pwd")
        except:
            raise ShibaCallingError("error : configuration file doesn't seem to be regular")
        self.init = MarketplaceManagement(ShibaConnection(login, pwd, "https://ws.sandbox.priceminister.com"))

    def test_get_product_list(self):
        """testing get_product_list methods with different queries, with some invalid ones as well"""
        try:
            obj = self.init.get_product_list()
        except ShibaParameterError:
            pass
        obj = self.init.get_product_list(kw="livre")
        self.assertTrue("listingresult" in obj.tag)
        try:
            obj = self.init.get_product_list(nbproductsperpage=-15, kw="livre")
        except ShibaParameterError:
            pass
        obj = self.init.get_product_list(kw="informatique", scope="PRICING")
        self.assertTrue("listingresult" in obj.tag)

    def test_get_category_map(self):
        """get_category_map regular test"""
        obj = self.init.get_category_map()
        self.assertTrue("categorymap" in obj.tag)