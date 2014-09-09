#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class InventoryManagementTest
# Testing InventoryManagement Class methods
#https://developer.priceminister.com/blog/fr/documentation/inventory-management/import-xml/product-types
#https://developer.priceminister.com/blog/fr/documentation/inventory-management/import-xml/product-type-template
#https://developer.priceminister.com/blog/fr/documentation/inventory-management/import-xml/generic-import-file0


from __future__ import unicode_literals

from Shiba.inventorymanagement import InventoryManagement
from Shiba.shibaconnection import ShibaConnection
from Shiba.shibaexceptions import *
from nose.tools import *

import unittest


class InventoryManagementTest(unittest.TestCase):

    def setUp(self):
        try:
            f = open("Assets/nosetests.cfg", "r")
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
        ptemplate = self.init.product_type_template(alias, "INVALIDSCOPE")

    def test_generic_import_file(self):
        """generic_import_file test, from an hand-written XML"""
        testdict =  {"item" : {"alias": "insolites_produit", "attributes" :
            {"advert" : {"attribute" : {"key" : "sellerReference", "value": "3069"}}, "product": {"attribute": [{"key": "submitterreference", "value": "Livre très vieux"},
                                                                         {"key": "title", "value": "livre vraiment tres vieux"},
                                                                         {"key": "sellerReference", "value": "SKU133755000"}]}}}}
        ret = self.init.generic_import_file(testdict)
        print(ret) #TODO des tests avec ET