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

import ConfigParser
import os
import mock
import xmltodict

import unittest

def return_quota_exceeded_messages(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/quota_exceeded_message.xml'))
    return datas.read()

class ShibaToolsTest(unittest.TestCase):
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
        self.init = ShibaTools()

    def test_retrieve_obj_from_url(self):
        """retrieve_obj_from_url test with a remote XML file"""
        obj = self.init.retrieve_obj_from_url("http://www.w3schools.com/xml/note.xml")
        self.assertTrue("note" in obj.content.tag)
        self.assertTrue("to" in obj.content.to.tag and obj.content.to == "Tove")
        self.assertTrue("heading" in obj.content.heading.tag and obj.content.heading == "Reminder")
        self.assertTrue("body" in obj.content.body.tag and obj.content.body == "Don't forget me this weekend!")

    def test_post_request(self):
        """testing a post request with retrieve_obj_from_url"""
        ret = self.init.post_request("http://postcatcher.in/catchers/54107375e4a183020000118c", "THIS IS SOME CONTENT")
        self.assertTrue(ret == "Created" or "Application Error" in ret)

    def test_create_obj_from_xml(self):
        """This function is entirely implicitely tested from the InventoryManagementTest.test_generic_import_file"""
        pass

    def test_inf_constructor(self):
        connection = ShibaConnection("test", "test")
        action = "genericimportreport"
        ret = self.init.inf_constructor(connection, action, inf1="info1", inf2="info2")
        self.assertTrue("inf1" in ret and "inf2" in ret)
        self.assertTrue(ret["inf1"] == "info1" and ret["action"] == "genericimportreport")

    def test_url_constructor(self):
        connection = ShibaConnection("test", "test")
        action = "genericimportreport"
        ret = self.init.inf_constructor(connection, action, inf1="info1", inf2="info2")
        url = self.init.url_constructor(connection, ret)
        self.assertTrue("https://ws.priceminister.com/stock_ws?pwd=test&version=2011-11-29&action=genericimportreport&"
                        "login=test&inf2=info2&inf1=info1" == url)

    @mock.patch('shiba.shibatools.ShibaTools.post_request', side_effect=return_quota_exceeded_messages)
    def test_assert_quota_exeeded(self, urlopen):
        """raise exception ShibaQuotaExceededError"""
        connection = ShibaConnection("test", "test")
        inventory = InventoryManagement(connection)
        f = open(os.path.dirname(os.path.realpath(__file__)) + "/Assets/genericimportfile.xml", "rb")
        testdict = xmltodict.parse(f)
        self.assertRaises(ShibaQuotaExceededError, inventory.generic_import_file, data=testdict)