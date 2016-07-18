# -*- coding: utf-8 -*-
""" Those exception classes will usually be raised after an error returned from the WebServices."""
from __future__ import unicode_literals


class ShibaException(Exception):
    """Main exception class, as you can catch the whole of Shiba exceptions from it"""
    pass


class ShibaParameterError(ShibaException):
    """Shiba parameter error, XML returned from the WebService told that one or more parameters are incorrect."""
    pass


class ShibaLoginError(ShibaException):
    """Shiba login error, XML returned from the WebService told that the login informations given are incorrect."""
    pass


class ShibaRightsError(ShibaException):
    """Shiba rights error, means XML returned the specified login IDs aren't authorized to access/modify such ressource
    from the asked WebService"""


class ShibaServiceError(ShibaException):
    """Shiba service error, WebService told that an error have been encountered, but may can't precise where"""
    pass


class ShibaUnknownServiceError(ShibaException):
    """Shiba unknown service error, WebService has caused/encoutered an error, but we can't know why (followed by a
    rough print of the XML retrieved"""
    pass


class ShibaConnectionError(ShibaException):
    """Shiba connection error, kind of an internal error: URL can't be reached, in case of bad URL formatting or
    internet connection failure (HTTP errors 404, 500...)."""
    pass


class ShibaCallingError(ShibaException):
    """Shiba internal error, for code relative errors. If such an exception is raised, look at given parameters to
    the API methods first as this is the major exception raising point for this type of exception"""
    pass


class ShibaQuotaExceededError(ShibaException):
    """Shiba throtlle error, you have sumbitted too many request of a type within a certain amount of time"""
    pass
