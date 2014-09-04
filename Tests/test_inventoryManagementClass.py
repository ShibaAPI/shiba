#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class InventoryManagementTest
# Testing InventoryManagement Class methods
#https://developer.priceminister.com/blog/fr/documentation/inventory-management/import-xml/product-types
#https://developer.priceminister.com/blog/fr/documentation/inventory-management/import-xml/product-type-template
#https://developer.priceminister.com/blog/fr/documentation/inventory-management/import-xml/generic-import-file0

import unittest
from Shiba.inventorymanagement import InventoryManagement


class InventoryManagementTest(unittest.TestCase):

    def setUp(self):
        #TODO Login infos as arguments for tests
        self.login = "nunux17"
        self.pwd = "ca9f0ccdc28c4005b56c2857722b113a"
        self.sandbox = "https://ws.sandbox.priceminister.com/"

    def product_types(self):
        """product_types return test"""

        im = InventoryManagement(self.login, self.pwd, self.sandbox)
        ptypes = im.product_types()
        self.assertTrue(ptypes.has_key("producttypesresult"))
"""
    def product_type_template(self):
""product_type_template tests on two scopes, for a fixed alias""
        alias = "mev_livre_livre_ancien"
        im = InventoryManagement(self.login, self.pwd, self.sandbox)
        ptemplate = im.product_type_template(alias, "")
        print(ptemplate)
        self.assertTrue(ptemplate.has_key("producttypetemplate"))
            """