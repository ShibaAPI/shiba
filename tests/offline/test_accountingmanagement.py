# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from shiba.accountingmanagement import AccountingManagement
from shiba.shibaconnection import ShibaConnection

from . import make_requests_get_mock


def test_get_operations(monkeypatch):
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_getoperations.xml'))
    account = AccountingManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    operations = account.get_operations()
    assert "getoperationsresult" in operations.content.tag
    assert operations.content.request.user == "vendeur"
    assert operations.content.request.operationcause == "salestransfer"


def test_get_compensation_details(monkeypatch):
    monkeypatch.setattr('requests.get', make_requests_get_mock('sample_getcompensationdetails.xml'))
    account = AccountingManagement(ShibaConnection("test", "test", "https://ws.sandbox.priceminister.com"))
    compensation_details = account.get_compensation_details("1337")
    assert compensation_details.content.tag == "getcompensationdetailsresult"
