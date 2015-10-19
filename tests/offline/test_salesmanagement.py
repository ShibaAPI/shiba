#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class SalesManagementTest
# Testing SalesManagement Class methods
# https://developer.priceminister.com/blog/fr/documentation/post-confirmation-of-sale
# https://developer.priceminister.com/blog/fr/documentation/new-sales

from __future__ import unicode_literals

from shiba.salesmanagement import SalesManagement
from shiba.shibaconnection import ShibaConnection
from shiba.shibaexceptions import *

import os

import unittest

import mock


def mock_get_new_sales(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_getnewsales.xml'))
    return datas


def mock_accept_sale(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_accept_sale.xml'))
    return datas


def mock_get_current_sales(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_getcurrentsales.xml'))
    return datas


def mock_get_billing_information(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_getbillinginformation.xml'))
    return datas


def mock_get_shipping_information(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_getshippinginformation.xml'))
    return datas


def mock_get_items_todo_list(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_getitemtodolist.xml'))
    return datas


def mock_get_item_infos(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_getiteminfos.xml'))
    return datas


def mock_cancel_item(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_cancelitem.xml'))
    return datas


def mock_contactus(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_contactus.xml'))
    return datas


def mock_contactuser(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_contactuser.xml'))
    return datas


def mock_set_tracking_package_infos(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_settrackingpackageinfos.xml'))
    return datas


def mock_confirm_preorder(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_confirmpreorder.xml'))
    return datas


class SalesManagementTest(unittest.TestCase):
    """SalesManagement class unit tests, as it's not possible to emulate a real seller profile, most of those tests
    are only verifying the proper handling of errors"""
    def setUp(self):
        self.init = SalesManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))

    @mock.patch('urllib2.urlopen', side_effect=mock_get_new_sales)
    def test_get_new_sales(self, urlopen):
        """regular get_new_sales test"""
        obj = self.init.get_new_sales()
        self.assertIn("getnewsalesresult", obj.content.tag)

    @mock.patch('urllib2.urlopen', side_effect=mock_accept_sale)
    def test_accept_sale(self, urlopen):
        """Only fail result, as accepting an actual sale is not simulable"""
        itemid = "000000"
        obj = None
        try:
            obj = self.init.accept_sale(itemid)
        except ShibaServiceError:
            pass
        except ShibaParameterError:
            pass

    @mock.patch('urllib2.urlopen', side_effect=mock_accept_sale)
    def test_refuse_sale(self, urlopen):
        """Only fail result, as refusing an actual sale is not simulable"""
        itemid = "000000"
        obj = None
        try:
            obj = self.init.refuse_sale(itemid)
        except ShibaServiceError:
            pass
        except ShibaParameterError:
            pass

    @mock.patch('urllib2.urlopen', side_effect=mock_get_current_sales)
    def test_get_current_sales(self, urlopen):
        """get_current_sales test, on variable parameters, plus some fail results"""
        obj = self.init.get_current_sales()
        self.assertIn("getcurrentsalesresult", obj.content.tag)
        self.assertFalse(obj.content.request.ispendingpreorder)
        try:
            self.init.get_current_sales(ispendingpreorder="n")
        except ShibaCallingError:
            pass
        obj = self.init.get_current_sales(purchasedate="WRONGDATE")
        self.assertTrue(elem.content.tag is not "purchasedate" for elem in obj.content.response)

    @mock.patch('urllib2.urlopen', side_effect=mock_get_billing_information)
    def test_get_billing_information(self, urlopen):
        """get_billing_information test, will raise an error due to unknown purchaseid"""
        obj = self.init.get_billing_information("1337")
        self.assertEqual(obj.content.tag, "getbillinginformationresult")

    @mock.patch('urllib2.urlopen', side_effect=mock_get_shipping_information)
    def test_get_shipping_information(self, urlopen):
        """get_billing_information test"""
        obj = None
        obj = self.init.get_shipping_information("1337")
        self.assertEqual(obj.content.tag, "getshippinginformationresult")

    @mock.patch('urllib2.urlopen', side_effect=mock_get_items_todo_list)
    def test_get_items_todo_list(self, urlopen):
        """get_items_todo_list routine test"""
        obj = self.init.get_item_todo_list()
        self.assertIn("getitemtodolistresult", obj.content.tag)

    @mock.patch('urllib2.urlopen', side_effect=mock_get_item_infos)
    def test_get_item_infos(self, urlopen):
        """get_item_infos on a product"""
        obj = self.init.get_item_infos("181063")
        self.assertEqual(obj.content.tag, "getiteminfosresult")

    @mock.patch('urllib2.urlopen', side_effect=mock_cancel_item)
    def test_cancel_item(self, urlopen):
        """cancel_item test"""
        obj = self.init.cancel_item("1337", "comment")
        self.assertEqual(obj.content.tag, "cancelitemresult")

    @mock.patch('urllib2.urlopen', side_effect=mock_contactus)
    def test_contact_us_about_item(self, urlopen):
        """contact_us_about_item test"""
        obj = self.init.contact_us_about_item("1337", "message", "1337")
        self.assertEqual(obj.content.tag, "contactusaboutitemresult")

    @mock.patch('urllib2.urlopen', side_effect=mock_contactuser)
    def test_contact_user_about_item(self, urlopen):
        """contact_user_about_item on a product"""
        obj = self.init.contact_user_about_item("1337", "message")
        self.assertEqual(obj.content.tag, "contactuseraboutitemresult")

    @mock.patch('urllib2.urlopen', side_effect=mock_set_tracking_package_infos)
    def test_set_tracking_package_infos(self, urlopen):
        """set_tracking_package_infos on a product. Testing internal error catching as well."""
        obj = self.init.set_tracking_package_infos("1337", "UPS", "0000000000")
        self.assertEqual(obj.content.tag, "setshippingpackageinfosresult")
        obj = None
        try:
            obj = self.init.set_tracking_package_infos("1337", "Autre", "0000000000")
        except ShibaCallingError:
            pass
        self.assertIsNone(obj)

    @mock.patch('urllib2.urlopen', side_effect=mock_confirm_preorder)
    def test_confirm_preorder(self, urlopen):
        """confirm_preorder on an advert. Testing internal error catching as well."""
        obj = self.init.confirm_preorder("1337", 1)
        self.assertEqual(obj.content.tag, "confirmpreorder")
        obj = None
        try:
            obj = self.init.confirm_preorder("1337", -8)
        except ShibaCallingError:
            pass
        self.assertIsNone(obj)
