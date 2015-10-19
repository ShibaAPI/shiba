#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class InventoryManagementTest
# Testing InventoryManagement Class methods
# https://developer.priceminister.com/blog/fr/documentation/inventory-management


from __future__ import unicode_literals

from shiba.inventorymanagement import InventoryManagement
from shiba.shibaconnection import ShibaConnection

import xmltodict
from lxml import objectify

import unittest

import os
import mock


def mock_product_types(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_getproducttypes.xml'))
    return datas


def mock_product_type_template(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_getproducttypetemplate.xml'))
    return datas


def mock_get_available_shipping_types(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_getavailableshippingtypes.xml'))
    return datas


def mock_export_inventory(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_exportinventory.xml'))
    return datas


def mock_generic_import_file(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_genericimportfile.xml'))
    return datas.read()


class InventoryManagementTest(unittest.TestCase):
    def setUp(self):
        self.init = InventoryManagement(ShibaConnection("test", "test", sandbox=True))

    @mock.patch('urllib2.urlopen', side_effect=mock_product_types)
    def test_product_types(self, urlopen):
        """product_types return test"""
        ptypes = self.init.product_types()
        self.assertIn("producttypesresult", ptypes.content.tag)

    @mock.patch('urllib2.urlopen', side_effect=mock_product_type_template)
    def test_product_type_template(self, urlopen):
        """product_type_template tests on two scopes, for a fixed alias, plus a fail result"""
        alias = "insolites_produit"
        ptemplate = self.init.product_type_template(alias, "")
        self.assertIn("producttypetemplateresult", ptemplate.content.tag)

    @mock.patch('shiba.shibatools.ShibaTools.post_request', side_effect=mock_generic_import_file)
    def test_generic_import_file(self, post_request):
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

    @mock.patch('urllib2.urlopen', side_effect=mock_get_available_shipping_types)
    def test_get_available_shipping_types(self, urlopen):
        obj = self.init.get_available_shipping_types()
        self.assertIn("getavailableshippingtypesresult", obj.content.tag)

    @mock.patch('urllib2.urlopen', side_effect=mock_export_inventory)
    def test_export_inventory(self, urlopen):
        obj = self.init.export_inventory()
        self.assertIn("inventoryresult", obj.content.tag)
