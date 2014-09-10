#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class ShibaToolsTest
# Unit tests each reachable method from ShibaTools class

from __future__ import unicode_literals

from Shiba.shibatools import ShibaTools
from Shiba.shibaexceptions import *
from Shiba.shibaconnection import ShibaConnection

import unittest

class ShibaToolsTest(unittest.TestCase):
    def setUp(self):
        try:
            f = open("Assets/nosetests.cfg", "r")
        except:
            raise ShibaCallingError("error : can't read login ID from the nosetests.cfg file")
        lines = [line.strip() for line in f]
        try:
            login = lines[0]
            pwd = lines[1]
            domain = lines[2]
        except:
            raise ShibaCallingError("error : configuration file doesn't seem to be regular")
        self.init = ShibaTools()

    def test_retrieve_obj_from_url(self):
        """retrieve_obj_from_url test with a remote XML file"""
        obj = self.init.retrieve_obj_from_url("http://www.w3schools.com/xml/note.xml")
        self.assertTrue("note" in obj.tag)
        self.assertTrue("to" in obj.to.tag and obj.to == "Tove")
        self.assertTrue("heading" in obj.heading.tag and obj.heading == "Reminder")
        self.assertTrue("body" in obj.body.tag and obj.body == "Don't forget me this weekend!")

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