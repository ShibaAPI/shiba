#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class AccountingManagementTest
# Testing AccountingManagement Class methods
# https://developer.priceminister.com/blog/fr/documentation/accounting


from __future__ import unicode_literals

from Shiba.accountingmanagement import AccountingManagement
from Shiba.shibaconnection import ShibaConnection
from Shiba.shibaexceptions import *

import unittest

from datetime import date


class AccountingManagementTest(unittest.TestCase):

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
        self.init = AccountingManagement(ShibaConnection(login, pwd, "https://ws.sandbox.priceminister.com"))

    def test_get_operations(self):
        """get_operations routine test, with date object as lastoperationdate too"""
        obj = self.init.get_operations()
        self.assertTrue("getoperationsresult" in obj.tag)
        obj = self.init.get_operations("21/12/2012-00:00:00")
        self.assertTrue(obj.request.lastoperationdate == "21/12/2012-00:00:00")
        testdate = date(2012, 12, 21)
        obj = self.init.get_operations(testdate)
        self.assertTrue(obj.request.lastoperationdate == "21/12/12-00:00:00")
        obj = None
        try:
            obj = self.init.get_operations("INVALIDDATE")
        except ShibaParameterError:
            pass
        self.assertTrue(obj is None)

    def test_get_compensation_details(self):
        """get_compensation_details test, must fail"""
        obj = None
        try:
            obj = self.init.get_compensation_details("1337")
        except ShibaParameterError:
            pass
        self.assertTrue(obj is None)
