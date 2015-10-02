#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class ShibaToolsTest
# Unit tests each reachable method from ShibaTools class

from __future__ import unicode_literals

from shiba.shibatools import ShibaTools
from shiba.shibaexceptions import *
from shiba.shibaconnection import ShibaConnection

from shiba.inventorymanagement import InventoryManagement

import os
import mock
import xmltodict

import unittest


def return_xml_for_url(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/note.xml'))
    return datas


def return_quota_exceeded_messages(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/quota_exceeded_message.xml'))
    return datas.read()


class ShibaToolsTest(unittest.TestCase):
    def setUp(self):
        self.init = ShibaTools()

    @mock.patch('urllib2.urlopen', side_effect=return_xml_for_url)
    def test_retrieve_obj_from_url(self, urlopen):
        """retrieve_obj_from_url test with a remote XML file"""
        obj = self.init.retrieve_obj_from_url("http://www.w3schools.com/xml/note.xml")
        self.assertIn("note", obj.content.tag)
        self.assertTrue("to" in obj.content.to.tag and obj.content.to == "Tove")
        self.assertTrue("heading" in obj.content.heading.tag and obj.content.heading == "Reminder")
        self.assertTrue("body" in obj.content.body.tag and obj.content.body == "Don't forget me this weekend!")

    def test_create_obj_from_xml(self):
        """This function is entirely implicitely tested from the InventoryManagementTest.test_generic_import_file"""
        pass

    def test_inf_constructor(self):
        connection = ShibaConnection("test", "test")
        action = "genericimportreport"
        ret = self.init.inf_constructor(connection, action, inf1="info1", inf2="info2")
        self.assertIn("inf1", ret)
        self.assertIn("inf2", ret)
        self.assertEqual(ret["inf1"], "info1")
        self.assertEqual(ret["action"], "genericimportreport")

    def test_url_constructor(self):
        connection = ShibaConnection("test", "test")
        action = "genericimportreport"
        ret = self.init.inf_constructor(connection, action, inf1="info1", inf2="info2")
        url = self.init.url_constructor(connection, ret)
        self.assertEqual("https://ws.priceminister.com/stock_ws?pwd=test&version=2011-11-29&action=genericimportreport&"
                         "login=test&inf2=info2&inf1=info1", url)

    @mock.patch('shiba.shibatools.ShibaTools.post_request', side_effect=return_quota_exceeded_messages)
    def test_assert_quota_exeeded(self, post_request):
        """raises ShibaQuotaExceededError exception"""
        connection = ShibaConnection("test", "test")
        inventory = InventoryManagement(connection)
        f = open(os.path.dirname(os.path.realpath(__file__)) + "/Assets/genericimportfile.xml", "rb")
        testdict = xmltodict.parse(f)
        self.assertRaises(ShibaQuotaExceededError, inventory.generic_import_file, data=testdict)
