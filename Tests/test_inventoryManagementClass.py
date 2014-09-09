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

import xmltodict
from lxml import objectify

import unittest
import pdb


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

    def test_product_type_template(self):
        """product_type_template tests on two scopes, for a fixed alias, plus a fail result"""
        alias = "insolites_produit"
        ptemplate = self.init.product_type_template(alias, "")
        self.assertTrue("producttypetemplateresult" in ptemplate.tag)
        ptemplate = self.init.product_type_template(alias, "VALUES")
        self.assertTrue("producttypetemplateresult" in ptemplate.tag)

    @raises(ShibaParameterError)
    def test_product_type_template_fail(self):
        self.init.product_type_template("INVALIDALIAS", "INVALIDSCOPE")

    def test_generic_import_file(self):
        """generic_import_file test, from an XML file. Conversion is done by xmltodict from a dict or OrderedDict
        , as well with objectify with an objectified ElementTree element"""
        f = open("Assets/genericimportfile.xml", "rb")
        testdict = xmltodict.parse(f)
        ret = self.init.generic_import_file(testdict)
        self.assertTrue("OK" == ret.response.status)
        f = open("Assets/genericimportfile.xml", "rb")
        testobj = objectify.parse(f)
        ret = self.init.generic_import_file(testobj)
        self.assertTrue("OK" == ret.response.status)

    def test_generic_import_report(self):
        f = open("Assets/genericimportfile.xml", "rb")
        testobj = objectify.parse(f)
        ret = self.init.generic_import_file(testobj)
        importid = ret.response.importid
        ret = self.init.generic_import_report(importid)
        pdb.set_trace()
        self.assertTrue("Reçu" == ret.response.file.status.text)