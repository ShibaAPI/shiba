#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class InventoryManagementTest
# Testing InventoryManagement Class methods
# https://developer.priceminister.com/blog/fr/documentation/inventory-management


from __future__ import unicode_literals

from shiba.inventorymanagement import InventoryManagement
from shiba.shibaconnection import ShibaConnection
from shiba.shibaexceptions import *
from nose.tools import *

import xmltodict
from lxml import objectify

import unittest

import ConfigParser
import os


class InventoryManagementTest(unittest.TestCase):

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
        self.init = InventoryManagement(ShibaConnection(login, pwd, "https://ws.sandbox.priceminister.com"))

    def test_product_types(self):
        """product_types return test"""

        ptypes = self.init.product_types()
        self.assertIn("producttypesresult", ptypes.content.tag)

    def test_product_type_template(self):
        """product_type_template tests on two scopes, for a fixed alias, plus a fail result"""

        alias = "insolites_produit"
        ptemplate = self.init.product_type_template(alias, "")
        self.assertIn("producttypetemplateresult", ptemplate.content.tag)
        ptemplate = self.init.product_type_template(alias, "VALUES")
        self.assertIn("producttypetemplateresult", ptemplate.content.tag)

    @raises(ShibaParameterError)
    def test_product_type_template_fail(self):
        self.init.product_type_template("INVALIDALIAS", "INVALIDSCOPE")

    def test_generic_import_file(self):
        """generic_import_file test, from an XML file. Conversion is done by xmltodict from a dict or OrderedDict
        , as well with objectify with an objectified ElementTree element"""

        f = open(os.path.dirname(os.path.realpath(__file__)) + "/Assets/genericimportfile.xml", "rb")
        testdict = xmltodict.parse(f)
        ret = self.init.generic_import_file(testdict)
        self.assertEqual("OK", ret.content.response.status)
        f = open(os.path.dirname(os.path.realpath(__file__)) + "/Assets/genericimportfile.xml", "rb")
        testobj = objectify.parse(f)
        ret = self.init.generic_import_file(testobj)
        self.assertEqual("OK", ret.content.response.status)

    def test_generic_import_report(self):
        """genreic_import_report method test from an import file call"""
        f = open(os.path.dirname(os.path.realpath(__file__)) + "/Assets/genericimportfile.xml", "rb")
        testobj = objectify.parse(f)
        ret = self.init.generic_import_file(testobj)
        importid = ret.content.response.importid
        ret = self.init.generic_import_report(importid)
        self.assertEqual("file", ret.content.response.file.filename)

    def test_get_available_shipping_types(self):
        try:
            self.init.get_available_shipping_types()
        except ShibaRightsError:
            pass

    def test_export_inventory(self):
        obj = self.init.export_inventory()
        self.assertIn("inventoryresult", obj.content.tag)
