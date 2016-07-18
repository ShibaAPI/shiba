# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from shiba.accountingmanagement import AccountingManagement
from shiba.shibaexceptions import ShibaParameterError

from datetime import date


def test_get_operations(connection):
    """get_operations routine test, with date object as lastoperationdate too"""
    accounting_management = AccountingManagement(connection)
    obj = accounting_management.get_operations()
    assert "getoperationsresult" in obj.content.tag
    obj = accounting_management.get_operations("21/12/2012-00:00:00")
    assert obj.content.request.lastoperationdate == "21/12/2012-00:00:00"
    testdate = date(2012, 12, 21)
    obj = accounting_management.get_operations(testdate)
    assert obj.content.request.lastoperationdate == "21/12/12-00:00:00"
    obj = None
    try:
        obj = accounting_management.get_operations("INVALIDDATE")
    except ShibaParameterError:
        pass
    assert obj is None


def test_get_compensation_details(connection):
    """get_compensation_details test, must fail"""
    accounting_management = AccountingManagement(connection)
    obj = None
    try:
        obj = accounting_management.get_compensation_details("1337")
    except ShibaParameterError:
        pass
    assert obj is None
