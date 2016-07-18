# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os.path as op
from shiba.inventorymanagement import InventoryManagement
from shiba.shibaconnection import ShibaConnection

import xmltodict
from lxml import objectify

from . import make_requests_get_mock, make_simple_text_mock


def test_product_types(monkeypatch):
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_getproducttypes.xml'))
    inventory_management = InventoryManagement(ShibaConnection("test", "test", sandbox=True))
    ptypes = inventory_management.product_types()
    assert "producttypesresult" in ptypes.content.tag


def test_product_type_template(monkeypatch):
    """product_type_template tests on two scopes, for a fixed alias, plus a fail result"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_getproducttypetemplate.xml'))
    alias = "insolites_produit"
    inventory_management = InventoryManagement(ShibaConnection("test", "test", sandbox=True))
    ptemplate = inventory_management.product_type_template(alias, "")
    assert "producttypetemplateresult" in ptemplate.content.tag


def test_get_available_shipping_types(monkeypatch):
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_getavailableshippingtypes.xml'))
    inventory_management = InventoryManagement(ShibaConnection("test", "test", sandbox=True))
    obj = inventory_management.get_available_shipping_types()
    assert "getavailableshippingtypesresult" in obj.content.tag


def test_export_inventory(monkeypatch):
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_exportinventory.xml'))
    inventory_management = InventoryManagement(ShibaConnection("test", "test", sandbox=True))
    obj = inventory_management.export_inventory()
    assert "inventoryresult" in obj.content.tag


def test_generic_import_file(monkeypatch):
    """generic_import_file test, from an XML file. Conversion is done by xmltodict from a dict or OrderedDict , as well
    with objectify with an objectified ElementTree element"""

    monkeypatch.setattr('shiba.shibatools.post_request', make_simple_text_mock('sample_genericimportfile.xml'))

    f = open(op.join(op.dirname(__file__), 'Assets', 'genericimportfile.xml'), 'rb')
    testdict = xmltodict.parse(f)
    inventory_management = InventoryManagement(ShibaConnection("test", "test", sandbox=True))
    ret = inventory_management.generic_import_file(testdict)
    assert "OK" == ret.content.response.status

    f = open(op.join(op.dirname(__file__), 'Assets', 'genericimportfile.xml'), 'rb')
    testobj = objectify.parse(f)
    inventory_management = InventoryManagement(ShibaConnection("test", "test", sandbox=True))
    ret = inventory_management.generic_import_file(testobj)
    assert "OK" == ret.content.response.status
