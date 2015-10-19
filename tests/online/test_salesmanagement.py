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

import unittest

import ConfigParser
import os


class SalesManagementTest(unittest.TestCase):
    """SalesManagement class unit tests, as it's not possible to emulate a real seller profile, most of those tests
    are only verifying the proper handling of errors"""
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
        self.init = SalesManagement(ShibaConnection(login, pwd, "https://ws.sandbox.priceminister.com"))

    def test_get_new_sales(self):
        """regular get_new_sales test"""
        obj = self.init.get_new_sales()
        self.assertTrue("getnewsalesresult" in obj.content.tag)

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
        self.assertIn("getcurrentsalesresult", obj.content.tag)
        self.assertFalse(obj.content.request.ispendingpreorder)
        obj = self.init.get_current_sales(ispendingpreorder="y")
        self.assertIn("getcurrentsalesresult", obj.content.tag)
        self.assertTrue(obj.content.request.ispendingpreorder)
        try:
            self.init.get_current_sales(ispendingpreorder="n")
        except ShibaCallingError:
            pass
        obj = self.init.get_current_sales(purchasedate="WRONGDATE")
        self.assertTrue(elem.content.tag is not "purchasedate" for elem in obj.content.response)
        obj = self.init.get_current_sales(purchasedate="2012-12-21")
        self.assertEqual("21/12/2012", obj.content.request.purchasedate)

    def test_get_billing_information(self):
        """get_billing_information test, will raise an error due to unknown purchaseid"""
        obj = None
        try:
            obj = self.init.get_billing_information("1337")
        except ShibaServiceError:
            pass
        self.assertIsNone(obj)

    def test_get_shipping_information(self):
        """get_billing_information test, will raise an error due to unknown purchaseid"""
        obj = None
        try:
            obj = self.init.get_shipping_information("1337")
        except ShibaServiceError:
            pass
        self.assertIsNone(obj)

    def test_get_items_todo_list(self):
        """get_items_todo_list routine test"""
        obj = self.init.get_item_todo_list()
        self.assertIn("getitemtodolistresult", obj.content.tag)

    def test_get_item_infos(self):
        """get_item_infos on a unknown product, must fail"""
        obj = None
        try:
            obj = self.init.get_item_infos("181063")
        except ShibaServiceError:
            pass
        self.assertIsNone(obj)

    def test_cancel_item(self):
        """cancel_item on an unknown product, must fail"""
        obj = None
        try:
            obj = self.init.cancel_item("1337", "comment")
        except ShibaServiceError:
            pass
        self.assertIsNone(obj)

    def test_contact_us_about_item(self):
        """contact_us_about_item on an unknown product, must fail"""
        obj = None
        try:
            obj = self.init.contact_us_about_item("1337", "message", "1337")
        except ShibaServiceError:
            pass
        self.assertIsNone(obj)

    def test_contact_user_about_item(self):
        """contact_user_about_item on an unknown product, must fail"""
        obj = None
        try:
            obj = self.init.contact_user_about_item("1337", "message")
        except ShibaServiceError:
            pass
        self.assertIsNone(obj)

    def test_set_tracking_package_infos(self):
        """set_tracking_package_infos on an unknown product, must fail. Testing internal error catching as well."""
        obj = None
        try:
            obj = self.init.set_tracking_package_infos("1337", "UPS", "0000000000")
        except ShibaParameterError:
            pass
        self.assertIsNone(obj)
        try:
            obj = self.init.set_tracking_package_infos("1337", "Autre", "0000000000")
        except ShibaCallingError:
            pass
        self.assertIsNone(obj)

    def test_confirm_preorder(self):
        """confirm_preorder on an unknown advert, must fail. Testing internal error catching as well."""
        obj = None
        try:
            obj = self.init.confirm_preorder("1337", 1)
        except ShibaParameterError:
            pass
        self.assertIsNone(obj)
        try:
            obj = self.init.confirm_preorder("1337", -8)
        except ShibaCallingError:
            pass
        self.assertIsNone(obj)

    def test_wrong_user(self):
        wronginstance = SalesManagement(ShibaConnection("test", "test"))
        try:
            obj = wronginstance.get_new_sales()
        except ShibaLoginError:
            pass
