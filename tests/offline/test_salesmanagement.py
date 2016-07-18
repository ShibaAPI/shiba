# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from shiba.salesmanagement import SalesManagement
from shiba.shibaconnection import ShibaConnection
from shiba.shibaexceptions import ShibaServiceError, ShibaParameterError, ShibaCallingError

from . import make_requests_get_mock


def test_get_new_sales(monkeypatch):
    """regular get_new_sales test"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_getnewsales.xml'))
    sales_management = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))

    obj = sales_management.get_new_sales()
    assert "getnewsalesresult" in obj.content.tag


def test_accept_sale(monkeypatch):
    """Only fail result, as accepting an actual sale is not simulable"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_accept_sale.xml'))
    sales_management = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    itemid = "000000"
    obj = None
    try:
        obj = sales_management.accept_sale(itemid)
    except ShibaServiceError:
        pass
    except ShibaParameterError:
        pass
    assert obj is not None


def test_refuse_sale(monkeypatch):
    """Only fail result, as refusing an actual sale is not simulable"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_accept_sale.xml'))
    sales_management = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    itemid = "000000"
    obj = None
    try:
        obj = sales_management.refuse_sale(itemid)
    except ShibaServiceError:
        pass
    except ShibaParameterError:
        pass
    assert obj is not None


def test_get_current_sales(monkeypatch):
    """get_current_sales test, on variable parameters, plus some fail results"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_getcurrentsales.xml'))
    sales_management = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    obj = sales_management.get_current_sales()
    assert "getcurrentsalesresult" in obj.content.tag
    assert not obj.content.request.ispendingpreorder
    try:
        sales_management.get_current_sales(ispendingpreorder="n")
    except ShibaCallingError:
        pass
    obj = sales_management.get_current_sales(purchasedate="WRONGDATE")
    for elem in obj.content.response:
        assert elem.tag != "purchasedate"


def test_get_billing_information(monkeypatch):
    """get_billing_information test, will raise an error due to unknown purchaseid"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_getbillinginformation.xml'))
    sales_management = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    obj = sales_management.get_billing_information("1337")
    assert obj.content.tag == "getbillinginformationresult"


def test_get_shipping_information(monkeypatch):
    """get_billing_information test"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_getshippinginformation.xml'))
    sales_management = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    obj = None
    obj = sales_management.get_shipping_information("1337")
    assert obj is not None
    assert obj.content.tag == "getshippinginformationresult"


def test_get_items_todo_list(monkeypatch):
    """get_items_todo_list routine test"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_getitemtodolist.xml'))
    sales_management = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    obj = sales_management.get_item_todo_list()
    assert "getitemtodolistresult" in obj.content.tag


def test_get_item_infos(monkeypatch):
    """get_item_infos on a product"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_getiteminfos.xml'))
    sales_management = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    obj = sales_management.get_item_infos("181063")
    assert obj.content.tag == "getiteminfosresult"


def test_cancel_item(monkeypatch):
    """cancel_item test"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_cancelitem.xml'))
    sales_management = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    obj = sales_management.cancel_item("1337", "comment")
    assert obj.content.tag == "cancelitemresult"


def test_contact_us_about_item(monkeypatch):
    """contact_us_about_item test"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_contactus.xml'))
    sales_management = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    obj = sales_management.contact_us_about_item("1337", "message", "1337")
    assert obj.content.tag == "contactusaboutitemresult"


def test_contact_user_about_item(monkeypatch):
    """contact_user_about_item on a product"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_contactuser.xml'))
    sales_management = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    obj = sales_management.contact_user_about_item("1337", "message")
    assert obj.content.tag == "contactuseraboutitemresult"


def test_set_tracking_package_infos(monkeypatch):
    """set_tracking_package_infos on a product. Testing internal error catching as well."""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_settrackingpackageinfos.xml'))
    sales_management = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    obj = sales_management.set_tracking_package_infos("1337", "UPS", "0000000000")
    assert obj.content.tag == "setshippingpackageinfosresult"
    obj = None
    try:
        obj = sales_management.set_tracking_package_infos("1337", "Autre", "0000000000")
    except ShibaCallingError:
        pass
    assert obj is None


def test_confirm_preorder(monkeypatch):
    """confirm_preorder on an advert. Testing internal error catching as well."""
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_confirmpreorder.xml'))
    sales_management = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    obj = sales_management.confirm_preorder("1337", 1)
    assert obj.content.tag == "confirmpreorder"
    obj = None
    try:
        obj = sales_management.confirm_preorder("1337", -8)
    except ShibaCallingError:
        pass
    assert obj is None
