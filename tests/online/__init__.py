# coding: utf-8
from __future__ import unicode_literals, print_function

import os
import ConfigParser

import pytest

from contextlib import contextmanager


@contextmanager
def assert_raises(exception_class, msg=None):
    """Check that an exception is raised and its message contains `msg`."""
    with pytest.raises(exception_class) as exception:
        yield
    if msg is not None:
        message = '%s' % exception
        assert msg.lower() in message.lower()


@pytest.fixture
def credentials():
    settings = ConfigParser.ConfigParser()
    settings.read(os.path.dirname(os.path.realpath(__file__)) + "/Assets/nosetests.cfg")
    return {'login': settings.get(str("NoseConfig"), "login"), 'password': settings.get(str("NoseConfig"), "pwd")}
