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
from shibatools import ShibaTools


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

    def product_type_template_test(self):
        """product_type_template tests on two scopes, for a fixed alias, plus a fail result"""
        alias = "insolites_produit"
        im = InventoryManagement(self.login, self.pwd, self.sandbox)
        ptemplate = im.product_type_template(alias, "")
        self.assertTrue("producttypetemplateresult" in ptemplate)
        ptemplate = im.product_type_template(alias, "VALUES")

        """
    def test_getProductTypeTemplate_1(self):
        ""test de getProductTypeTemplate""

        alias = 'mev_livre_livre_ancien'
        inventorymanagement = InventoryManagementClass(self.login, self.pwd, self.version)
        attributes_list_result = inventorymanagement.getProductTypeTemplate(alias)
        self.assertTrue(len(attributes_list_result) > 0)

    def test_createInventoryFile_1(self):
        ""test de createInventoryFile""

        items = {
            'alias1': {
                'productattributes': {
                    'codebarres': 'EAN1234567890',
                    'pid': 'PID1234567890',
                },
                'advertattributes': {
                    'sellerReference': 'SKU12345SKU_1234567890',
                    'sellingPrice': 35,
                    'state': 15,
                    'comment': 'super article!',
                    'qty': 3,
                },
            },
            'alias2': {
                'productattributes': {
                    'codebarres': 'EAN1234567890',
                    'pid': 'PID1234567890',
                },
                'advertattributes': {
                    'sellerReference': 'SKU12345SKU_1234567890',
                    'sellingPrice': 35,
                    'state': 15,
                    'comment': 'super article!',
                    'qty': 3,
                },
            },
        }
        inventorymanagement = InventoryManagementClass(self.login, self.pwd, self.version)
        xml_result = inventorymanagement.createInventoryFile(items)
        self.assertTrue(len(xml_result) > 0) #TODO des tests avec ET

"""