#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os.path as op
import xmltodict

from shiba.shibatools import inf_constructor, retrieve_obj_from_url, url_constructor
from shiba.shibaexceptions import ShibaQuotaExceededError
from shiba.shibaconnection import ShibaConnection

from shiba.inventorymanagement import InventoryManagement

from . import make_requests_get_mock, make_simple_text_mock, assert_raises


def test_retrieve_obj_from_url(monkeypatch):
    """retrieve_obj_from_url test with a remote XML file"""
    monkeypatch.setattr('requests.get', make_requests_get_mock('note.xml'))
    obj = retrieve_obj_from_url("http://www.w3schools.com/xml/note.xml")
    assert "note" in obj.content.tag
    assert "to" in obj.content.to.tag and obj.content.to == "Tove"
    assert "heading" in obj.content.heading.tag and obj.content.heading == "Reminder"
    assert "body" in obj.content.body.tag and obj.content.body == "Don't forget me this weekend!"


def test_inf_constructor():
    connection = ShibaConnection("test", "test")
    action = "genericimportreport"
    ret = inf_constructor(connection, action, inf1="info1", inf2="info2")
    assert "inf1" in ret
    assert "inf2" in ret
    assert ret["inf1"] == "info1"
    assert ret["action"] == "genericimportreport"


def test_url_constructor_with_accent():
    connection = ShibaConnection("test", "test")
    action = "genericimportreport"
    ret = inf_constructor(connection, action, inf1=u"é", inf2=u"à")
    url = url_constructor(connection, ret)
    assert ("https://ws.priceminister.com/stock_ws?action=genericimportreport&inf1=%C3%A9&inf2=%C3%A0&login=test&"
            "pwd=test&version=2011-11-29" == url)


def test_url_constructor():
    connection = ShibaConnection("test", "test")
    action = "genericimportreport"
    ret = inf_constructor(connection, action, inf1="info1", inf2="info2")
    url = url_constructor(connection, ret)
    assert ("https://ws.priceminister.com/stock_ws?action=genericimportreport&inf1=info1&inf2=info2&login=test&"
            "pwd=test&version=2011-11-29" == url)


def test_assert_quota_exeeded(monkeypatch):
    """raises ShibaQuotaExceededError exception"""
    monkeypatch.setattr('shiba.shibatools.post_request', make_simple_text_mock('quota_exceeded_message.xml'))

    connection = ShibaConnection("test", "test")
    inventory = InventoryManagement(connection)
    f = open(op.join(op.dirname(__file__), 'Assets', 'genericimportfile.xml'), 'rb')
    testdict = xmltodict.parse(f)
    with assert_raises(ShibaQuotaExceededError):
        inventory.generic_import_file(data=testdict)
