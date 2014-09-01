#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# testClassPlateforme
# permet de tester unitairement la classe plateforme

#TODO tests sur la plateforme de tests de priceminister
#https://developer.priceminister.com/blog/fr/documentation/inventory-management/import-xml/product-types
#https://developer.priceminister.com/blog/fr/documentation/inventory-management/import-xml/product-type-template
#https://developer.priceminister.com/blog/fr/documentation/inventory-management/import-xml/generic-import-file0

from nose.tools import *

from ..brouillons.shiba.shiba.shiba.InventoryManagement.inventoryManagementClass import InventoryManagementClass


class test_inventoryManagementClass(unittest.TestCase):

    def setUp(self):
        self.login = 'login'
        self.pwd = 'pwd'
        self.version = 'version'

    def test_getProductTypes_1(self):
        """test de getProductTypes"""

        inventorymanagement = InventoryManagementClass(self.login, self.pwd, self.version)
        alias_list_result = inventorymanagement.getProductTypes()
        self.assertTrue(len(alias_list_result) > 0)

    def test_getProductTypeTemplate_1(self):
        """test de getProductTypeTemplate"""

        alias = 'mev_livre_livre_ancien'
        inventorymanagement = InventoryManagementClass(self.login, self.pwd, self.version)
        attributes_list_result = inventorymanagement.getProductTypeTemplate(alias)
        self.assertTrue(len(attributes_list_result) > 0)

    def test_createInventoryFile_1(self):
        """test de createInventoryFile"""

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

