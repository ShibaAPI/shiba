#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class ShibaToolsTest
# Unit tests each reachable method from ShibaTools class

from __future__ import unicode_literals

from shiba.shibatools import ShibaTools
from shiba.shibaexceptions import *
from shiba.shibaconnection import ShibaConnection

import ConfigParser
import os

import unittest


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
        self.assertIn("note", obj.content.tag)
        self.assertTrue("to" in obj.content.to.tag and obj.content.to == "Tove")
        self.assertTrue("heading" in obj.content.heading.tag and obj.content.heading == "Reminder")
        self.assertTrue("body" in obj.content.body.tag and obj.content.body == "Don't forget me this weekend!")

    def test_post_request(self):
        """
        Testing a post request with retrieve_obj_from_url
        This test method is dependant of the service used.
        (i.e., the content of the assert would change if the test service changes).
        http://httpbin.org/post returns the POST data you send.
        """
        post_data = "Who do you think you are to give me advice about dating?"
        ret = self.init.post_request("http://httpbin.org/post", post_data)
        self.assertIn(post_data, ret)

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
