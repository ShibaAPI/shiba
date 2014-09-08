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
from Shiba.shibaconnection import ShibaConnection
from Shiba.shibaexceptions import *
from nose.tools import *
from lxml import objectify
import pdb
from lxml import objectify


class InventoryManagementTest(unittest.TestCase):

    def setUp(self):
        try:
            f = open("nosetests.cfg", "r")
        except:
            raise ShibaCallingError("error : can't read login ID from the nosetests.cfg file")
        lines = [line.strip() for line in f]
        try:
            login = lines[0]
            pwd = lines[1]
            domain = lines[2]
        except:
            raise ShibaCallingError("error : configuration file doesn't seem to be regular")
        self.init = InventoryManagement(ShibaConnection(login, pwd, domain))

    def test_product_types(self):
        """product_types return test"""

        ptypes = self.init.product_types()
        self.assertTrue("producttypesresult" in ptypes.tag)

    @raises(ShibaParameterError)
    def test_product_type_template(self):
        """product_type_template tests on two scopes, for a fixed alias, plus a fail result"""
        alias = "insolites_produit"
        ptemplate = self.init.product_type_template(alias, "")
        self.assertTrue("producttypetemplateresult" in ptemplate.tag)
        ptemplate = self.init.product_type_template(alias, "VALUES")
        self.assertTrue("producttypetemplateresult" in ptemplate.tag)
        ptemplate = None
        ptemplate = self.init.product_type_template(alias, "INVALIDSCOPE")

"""
    def test_generic_import_file(self):
        ""generic_import_file test, from a hand-written XML""
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
        ret = self.init.generic_import_file(items)
        print(ret)
        self.assertTrue(len(xml_result) > 0) #TODO des tests avec ET"""