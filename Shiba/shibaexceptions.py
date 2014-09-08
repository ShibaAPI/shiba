#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class ShibaException and inherited ones
# Shiba exceptions classes


"""Those exception classes will usually be raised after an error returned from the WebServices"""
class   ShibaException(Exception):
    """Main exception class, as you can catch the whole of Shiba exceptions from it"""
    pass

class   ShibaParameterError(ShibaException):
    """Shiba parameter error, XML returned from the WebService told that one or more parameters are incorrect."""
    pass

class   ShibaLoginError(ShibaException):
    """Shiba login error, XML returner from the WebService told that the login informations given are incorrect."""
    pass

class   ShibaConnectionError(ShibaException):
    """Shiba connection error, kind of an internal error: URL can't be reached, in case of bad URL formatting or
    internet connection failure (HTTP errors 404, 500...)."""
    pass

class   ShibaUnknownError(ShibaException):
    """Exception for all other errors that can't be precisely defined."""
    pass

class   ShibaCallingError(ShibaException):
    """Shiba internal error, for code relative errors. If such an exception is raised, look at given parameters to
    the API methods first as this is the major exception raising point for this type of exception"""
    pass

