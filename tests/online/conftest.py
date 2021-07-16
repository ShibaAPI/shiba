# coding: utf-8
import os

import pytest

from shiba.shibaconnection import ShibaConnection


ONLINE_TEST_ENABLED = os.environ.get("SHIBA_API_LOGIN", None) is not None


def get_connection():
    login = os.environ["SHIBA_API_LOGIN"]
    password = os.environ["SHIBA_API_PASSWORD"]
    return ShibaConnection(login, password, "https://ws.fr.shopping.rakuten.com")


def check_sandbox_up():
    if ONLINE_TEST_ENABLED:
        # connection = get_connection()
        # TODO: handle HTTP 50x error, to skip online test
        # import pdb; pdb.set_trace()  # noqa
        return True


@pytest.fixture
@pytest.mark.skipif(not check_sandbox_up(), reason="need access to the sandbox")
def connection():
    return get_connection()


@pytest.fixture
def fake_connection():
    return ShibaConnection(
        "Qvuik5bZVHbmg4mWsdsd0ik9",
        "RInDsddsdsdZ72tfA",
        "https://ws.fr.shopping.rakuten.com",
    )
