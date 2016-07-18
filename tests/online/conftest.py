# coding: utf-8
from __future__ import unicode_literals, print_function

import os
import ConfigParser

import pytest

from shiba.shibaconnection import ShibaConnection


@pytest.fixture
def connection():
    settings = ConfigParser.ConfigParser()
    settings.read(os.path.dirname(os.path.realpath(__file__)) + "/Assets/nosetests.cfg")
    login = settings.get(str("NoseConfig"), "login")
    password = settings.get(str("NoseConfig"), "pwd")
    return ShibaConnection(login, password, "https://ws.sandbox.priceminister.com")


@pytest.fixture
def fake_connection():
    return ShibaConnection("Qvuik5bZVHbmg4mWsdsd0ik9", "RInDsddsdsdZ72tfA", "https://ws.sandbox.priceminister.com")
