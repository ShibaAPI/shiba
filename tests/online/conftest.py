# coding: utf-8
from __future__ import unicode_literals, print_function

import os

import pytest

from shiba.shibaconnection import ShibaConnection


ONLINE_TEST_DISABLED = os.environ.get("SHIBA_API_LOGIN", None) is None


@pytest.fixture(params=[pytest.mark.skipif(ONLINE_TEST_DISABLED,  reason='need online credentials')('parameter')])
def connection():
    login = os.environ['SHIBA_API_LOGIN']
    password = os.environ['SHIBA_API_PASSWORD']
    return ShibaConnection(login, password, "https://ws.sandbox.priceminister.com")


@pytest.fixture
def fake_connection():
    return ShibaConnection("Qvuik5bZVHbmg4mWsdsd0ik9", "RInDsddsdsdZ72tfA", "https://ws.sandbox.priceminister.com")
