# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from shiba.shibatools import inf_constructor, retrieve_obj_from_url, url_constructor, post_request
from shiba.shibaconnection import ShibaConnection


def test_retrieve_obj_from_url():
    """retrieve_obj_from_url test with a remote XML file"""
    obj = retrieve_obj_from_url("http://www.w3schools.com/xml/note.xml")
    assert "note" in obj.content.tag
    assert "to" in obj.content.to.tag and obj.content.to == "Tove"
    assert "heading" in obj.content.heading.tag and obj.content.heading == "Reminder"
    assert "body" in obj.content.body.tag and obj.content.body == "Don't forget me this weekend!"


def test_post_request():
    """
    Testing a post request with retrieve_obj_from_url
    This test method is dependant of the service used.
    (i.e., the content of the assert would change if the test service changes).
    http://httpbin.org/post returns the POST data you send.
    """
    post_data = "Who do you think you are to give me advice about dating?"
    ret = post_request("http://httpbin.org/post", post_data)
    assert post_data in ret


def test_inf_constructor():
    connection = ShibaConnection("test", "test")
    action = "genericimportreport"
    ret = inf_constructor(connection, action, inf1="info1", inf2="info2")
    assert "inf1" in ret
    assert "inf2" in ret
    assert ret["inf1"] == "info1"
    assert ret["action"] == "genericimportreport"


def test_url_constructor(fake_connection):
    connection = ShibaConnection("test", "test")
    action = "genericimportreport"
    ret = inf_constructor(connection, action, inf1="info1", inf2="info2")
    url = url_constructor(connection, ret)
    assert (url == "https://ws.priceminister.com/stock_ws?action=genericimportreport&inf1=info1&inf2=info2&login"
                   "=test&pwd=test&version=2011-11-29")
