#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class AccountingManagementTest
# Testing AccountingManagement Class methods
# https://developer.priceminister.com/blog/fr/documentation/accounting


from __future__ import unicode_literals

from shiba.accountingmanagement import AccountingManagement
from shiba.shibaconnection import ShibaConnection

import os

import unittest
import mock


def mock_get_operations(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_getoperations.xml'))
    return datas


def mock_get_compensation_details(*args, **kwargs):
    datas = open(os.path.join(os.path.dirname(__file__), 'Assets/sample_getcompensationdetails.xml'))
    return datas


class AccountingManagementTest(unittest.TestCase):

    def setUp(self):
        self.init = AccountingManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))

    @mock.patch('urllib2.urlopen', side_effect=mock_get_operations)
    def test_get_operations(self, urlopen):
        """get_operations routine test"""
        obj = self.init.get_operations()
        self.assertIn("getoperationsresult", obj.content.tag)
        self.assertEqual(obj.content.request.user, "vendeur")
        self.assertEqual(obj.content.request.operationcause, "salestransfer")

    @mock.patch('urllib2.urlopen', side_effect=mock_get_compensation_details)
    def test_get_compensation_details(self, urlopen):
        """get_compensation_details test"""
        obj = self.init.get_compensation_details("1337")
        self.assertEqual(obj.content.tag, "getcompensationdetailsresult")
