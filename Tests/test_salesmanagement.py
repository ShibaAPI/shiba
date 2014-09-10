#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class SalesManagementTest
# Testing SalesManagement Class methods
# https://developer.priceminister.com/blog/fr/documentation/post-confirmation-of-sale
# https://developer.priceminister.com/blog/fr/documentation/new-sales

from __future__ import unicode_literals

from Shiba.salesmanagement import SalesManagement
from Shiba.shibaconnection import ShibaConnection
from Shiba.shibaexceptions import *

import unittest

class SalesManagementTest(unittest.TestCase):
    """SalesManagement class unit tests, as it's not possible to emulate a real seller profile, most of those tests
    are only verifying the proper handling of errors"""
    def setUp(self):
        try:
            f = open("Assets/nosetests.cfg", "r")
        except:
            raise ShibaCallingError("error : can't read login ID from the nosetests.cfg file")
        lines = [line.strip() for line in f]
        try:
            login = lines[0]
            pwd = lines[1]
            domain = "https://ws.sandbox.priceminister.com"
        except:
            raise ShibaCallingError("error : configuration file doesn't seem to be regular")
        self.init = SalesManagement(ShibaConnection(login, pwd, "https://ws.sandbox.priceminister.com"))

    def test_get_new_sales(self):
        """regular get_new_sales test"""
        obj = self.init.get_new_sales()
        self.assertTrue("getnewsalesresult" in obj.tag)

    def test_accept_sale(self):
        """Only fail result, as accepting an actual sale is not simulable"""
        itemid = "000000"
        obj = None
        try:
            obj = self.init.accept_sale(itemid)
        except ShibaServiceError:
            pass
        except ShibaParameterError:
            pass

    def test_refuse_sale(self):
        """Only fail result, as refusing an actual sale is not simulable"""
        itemid = "000000"
        obj = None
        try:
            obj = self.init.refuse_sale(itemid)
        except ShibaServiceError:
            pass
        except ShibaParameterError:
            pass

    def test_get_current_sales(self):
        """get_current_sales test, on variable parameters, plus some fail results"""
        obj = self.init.get_current_sales()
        self.assertTrue("getcurrentsalesresult" in obj.tag)
        self.assertTrue(False == obj.request.ispendingpreorder)
        obj = self.init.get_current_sales(ispendingpreorder="y")
        self.assertTrue("getcurrentsalesresult" in obj.tag)
        self.assertTrue(True == obj.request.ispendingpreorder)
        try:
            self.init.get_current_sales(ispendingpreorder="n")
        except ShibaCallingError:
            pass
        obj = self.init.get_current_sales(purchasedate="WRONGDATE")
        self.assertTrue(elem.tag is not "purchasedate" for elem in obj.response)
        obj = self.init.get_current_sales(purchasedate="2012-12-21")
        self.assertTrue("21/12/2012" == obj.request.purchasedate)

    def test_get_billing_information(self):
        """get_billing_information test, will raise an error due to unknown purchaseid"""
        obj = None
        try:
            obj = self.init.get_billing_information("1337")
        except ShibaServiceError:
            pass
        self.assertTrue(obj is None)

    def test_get_shipping_information(self):
        """get_billing_information test, will raise an error due to unknown purchaseid"""
        obj = None
        try:
            obj = self.init.get_shipping_information("1337")
        except ShibaServiceError:
            pass
        self.assertTrue(obj is None)

    def test_get_items_todo_list(self):
        """get_items_todo_list routine test"""
        obj = self.init.get_item_todo_list()
        self.assertTrue("getitemtodolistresult" in obj.tag)

    def test_get_item_infos(self):
        """get_item_infos on a unknown product, must fail"""
        obj = None
        try:
            obj = self.init.get_item_infos("181063")
        except ShibaServiceError:
            pass
        self.assertTrue(obj is None)

    def test_cancel_item(self):
        """cancel_item on an unknown product, must fail"""
        obj = None
        try:
            obj = self.init.cancel_item("1337", "comment")
        except ShibaServiceError:
            pass
        self.assertTrue(obj is None)

    def test_contact_us_about_item(self):
        """contact_us_about_item on an unknown product, must fail"""
        obj = None
        try:
            obj = self.init.contact_us_about_item("1337", "message")
        except ShibaServiceError:
            pass
        self.assertTrue(obj is None)

    def test_contact_user_about_item(self):
        """contact_user_about_item on an unknown product, must fail"""
        obj = None
        try:
            obj = self.init.contact_user_about_item("1337", "message")
        except ShibaServiceError:
            pass
        self.assertTrue(obj is None)

    def test_set_tracking_package_infos(self):
        """set_tracking_package_infos on an unknown product, must fail. Testing internal error catching as well."""
        obj = None
        try:
            obj = self.init.set_tracking_package_infos("1337", "UPS", "0000000000")
        except ShibaParameterError:
            pass
        self.assertTrue(obj is None)
        try:
            obj = self.init.set_tracking_package_infos("1337", "Autre", "0000000000")
        except ShibaCallingError:
            pass
        self.assertTrue(obj is None)

    def test_confirm_preorder(self):
        """confirm_preorder on an unknown advert, must fail. Testing internal error catching as well."""
        obj = None
        try:
            obj = self.init.confirm_preorder("1337", 1)
        except ShibaParameterError:
            pass
        self.assertTrue(obj is None)
        try:
            obj = self.init.confirm_preorder("1337", -8)
        except ShibaCallingError:
            pass
        self.assertTrue(obj is None)

    def test_wrong_user(self):
        wronginstance = SalesManagement(ShibaConnection("test", "test"))
        try:
            obj = wronginstance.get_new_sales()
        except ShibaLoginError:
            pass
