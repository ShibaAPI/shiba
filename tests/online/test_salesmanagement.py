# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from shiba.salesmanagement import SalesManagement
from shiba.shibaexceptions import *


def test_get_new_sales(connection):
    """regular get_new_sales test"""
    sales_management = SalesManagement(connection)
    obj = sales_management.get_new_sales()
    assert "getnewsalesresult" in obj.content.tag


def test_accept_sale(connection):
    """Only fail result, as accepting an actual sale is not simulable"""
    sales_management = SalesManagement(connection)
    itemid = "000000"
    obj = None
    try:
        obj = sales_management.accept_sale(itemid)
    except ShibaServiceError:
        pass
    except ShibaParameterError:
        pass


def test_refuse_sale(connection):
    """Only fail result, as refusing an actual sale is not simulable"""
    sales_management = SalesManagement(connection)
    itemid = "000000"
    obj = None
    try:
        obj = sales_management.refuse_sale(itemid)
    except ShibaServiceError:
        pass
    except ShibaParameterError:
        pass


def test_get_current_sales(connection):
    """get_current_sales test, on variable parameters, plus some fail results"""
    sales_management = SalesManagement(connection)
    obj = sales_management.get_current_sales()
    assert "getcurrentsalesresult" in obj.content.tag
    assert not obj.content.request.ispendingpreorder
    obj = sales_management.get_current_sales(ispendingpreorder="y")
    assert "getcurrentsalesresult" in obj.content.tag
    assert obj.content.request.ispendingpreorder
    try:
        sales_management.get_current_sales(ispendingpreorder="n")
    except ShibaCallingError:
        pass
    obj = sales_management.get_current_sales(purchasedate="WRONGDATE")
    for elem in obj.content.response:
        assert elem.tag != "purchasedate"
    obj = sales_management.get_current_sales(purchasedate="2012-12-21")
    assert "21/12/2012" == obj.content.request.purchasedate


def test_get_billing_information(connection):
    """get_billing_information test, will raise an error due to unknown purchaseid"""
    sales_management = SalesManagement(connection)
    obj = None
    try:
        obj = sales_management.get_billing_information("1337")
    except ShibaServiceError:
        pass
    assert obj is None


def test_get_shipping_information(connection):
    """get_billing_information test, will raise an error due to unknown purchaseid"""
    sales_management = SalesManagement(connection)
    obj = None
    try:
        obj = sales_management.get_shipping_information("1337")
    except ShibaServiceError:
        pass
    assert obj is None


def test_get_items_todo_list(connection):
    """get_items_todo_list routine test"""
    sales_management = SalesManagement(connection)
    obj = sales_management.get_item_todo_list()
    assert "getitemtodolistresult" in obj.content.tag


def test_get_item_infos(connection):
    """get_item_infos on a unknown product, must fail"""
    sales_management = SalesManagement(connection)
    obj = None
    try:
        obj = sales_management.get_item_infos("181063")
    except ShibaServiceError:
        pass
    assert obj is None


def test_cancel_item(connection):
    """cancel_item on an unknown product, must fail"""
    sales_management = SalesManagement(connection)
    obj = None
    try:
        obj = sales_management.cancel_item("1337", "comment")
    except ShibaServiceError:
        pass
    assert obj is None


def test_contact_us_about_item(connection):
    """contact_us_about_item on an unknown product, must fail"""
    sales_management = SalesManagement(connection)
    obj = None
    try:
        obj = sales_management.contact_us_about_item("1337", "message", "1337")
    except ShibaServiceError:
        pass
    assert obj is None


def test_contact_user_about_item(connection):
    """contact_user_about_item on an unknown product, must fail"""
    sales_management = SalesManagement(connection)
    obj = None
    try:
        obj = sales_management.contact_user_about_item("1337", "message")
    except ShibaServiceError:
        pass
    assert obj is None


def test_set_tracking_package_infos(connection):
    """set_tracking_package_infos on an unknown product, must fail. Testing internal error catching as well."""
    sales_management = SalesManagement(connection)
    obj = None
    try:
        obj = sales_management.set_tracking_package_infos("1337", "UPS", "0000000000")
    except ShibaParameterError:
        pass
    assert obj is None
    try:
        obj = sales_management.set_tracking_package_infos("1337", "Autre", "0000000000")
    except ShibaCallingError:
        pass
    assert obj is None


def test_confirm_preorder(connection):
    """confirm_preorder on an unknown advert, must fail. Testing internal error catching as well."""
    sales_management = SalesManagement(connection)
    obj = None
    try:
        obj = sales_management.confirm_preorder("1337", 1)
    except ShibaParameterError:
        pass
    assert obj is None
    try:
        obj = sales_management.confirm_preorder("1337", -8)
    except ShibaCallingError:
        pass
    assert obj is None


def test_wrong_user(fake_connection):
    sales_management = SalesManagement(fake_connection)
    try:
        sales_management.get_new_sales()
    except ShibaLoginError:
        pass
