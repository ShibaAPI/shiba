# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from shiba.shibaexceptions import ShibaRightsError
from shiba.inventorymanagement import InventoryManagement

import xmltodict
from lxml import objectify

import os


def test_product_types(connection):
    """product_types return test"""
    inventory_management = InventoryManagement(connection)
    ptypes = inventory_management.product_types()
    assert "producttypesresult" in ptypes.content.tag


def test_product_type_template(connection):
    """product_type_template tests on two scopes, for a fixed alias, plus a fail result"""
    inventory_management = InventoryManagement(connection)
    alias = "insolites_produit"
    ptemplate = inventory_management.product_type_template(alias, "")
    assert "producttypetemplateresult" in ptemplate.content.tag
    ptemplate = inventory_management.product_type_template(alias, "VALUES")
    assert "producttypetemplateresult" in ptemplate.content.tag


# @raises(ShibaParameterError)
# def test_product_type_template_fail(connection):
#     inventory_management = InventoryManagement(connection)
#     inventory_management.product_type_template("INVALIDALIAS", "INVALIDSCOPE")


def test_generic_import_file(connection):
    """generic_import_file test, from an XML file. Conversion is done by xmltodict from a dict or OrderedDict
    , as well with objectify with an objectified ElementTree element"""
    inventory_management = InventoryManagement(connection)

    f = open(os.path.dirname(os.path.realpath(__file__)) + "/Assets/genericimportfile.xml", "rb")
    testdict = xmltodict.parse(f)
    ret = inventory_management.generic_import_file(testdict)
    assert "OK" == ret.content.response.status

    f = open(os.path.dirname(os.path.realpath(__file__)) + "/Assets/genericimportfile.xml", "rb")
    testobj = objectify.parse(f)
    ret = inventory_management.generic_import_file(testobj)
    assert "OK" == ret.content.response.status


def test_generic_import_report(connection):
    """genreic_import_report method test from an import file call"""
    inventory_management = InventoryManagement(connection)
    f = open(os.path.dirname(os.path.realpath(__file__)) + "/Assets/genericimportfile.xml", "rb")
    testobj = objectify.parse(f)
    ret = inventory_management.generic_import_file(testobj)
    importid = ret.content.response.importid
    ret = inventory_management.generic_import_report(importid)
    assert "file" == ret.content.response.file.filename


def test_get_available_shipping_types(connection):
    inventory_management = InventoryManagement(connection)
    try:
        inventory_management.get_available_shipping_types()
    except ShibaRightsError:
        pass


# def test_export_inventory(connection):
#     """
#     This test fails if you do not use a PRO ACCOUNT.
#     :return:
#     """
#     inventory_management = InventoryManagement(connection)
#     print("This test fails if you do not use a PRO ACCOUNT.")
#     obj = inventory_management.export_inventory()
#     assert "inventoryresult" in obj.content.tag
