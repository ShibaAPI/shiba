#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class ShibaTools
# Shiba runtime tools class

import httplib
import urllib2 as ul

from lxml import objectify
from lxml import etree

from shibaconnection import ShibaConnection
from shibaexceptions import *

import xmltodict


"""Tools used by Shiba data retrieving classes"""
class ShibaTools(object):
    @staticmethod
    def __errors_check(obj):
        """Errors checking from the returned XML as object."""
        if "errorresponse" in obj.tag:
            if "ParameterError" == obj.error.code:
                raise ShibaParameterError("Parameter error : " + obj.error.message +
                " Reason : " + obj.error.details.detail)
            if "InvalidUserConnection" == obj.error.code:
                raise ShibaLoginError("Invalid user connection : " + obj.errorresponse.error.message +
                " Reason : " + obj.error.details.detail)
            return True
        return False

    @staticmethod
    def retrieve_obj_from_url(url):
        """Give it an , will send you back a instanced object based on received XML from WebService.
        :rtype : lxml.objectivy class"""
        try:
            xml = ul.urlopen(url).read()
        except ul.HTTPError, e:
            raise ShibaConnectionError("HTTP error = " + str(e.code) + " - On URL: " + url)
        except ul.URLError, e:
            raise ShibaConnectionError("URL error = " + str(e.reason) + " - On URL: " + url)
        except httplib.HTTPException:
            raise ShibaUnknownError("HTTP unknown error =" + " - On URL: " + url)
        obj = objectify.fromstring(xml)
        ShibaTools.__errors_check(obj)
        return obj

    @staticmethod
    def create_xml_from_item_obj(inv):
        """Generate XML from the "inv" parameter, which is an object hierarchized as the XML structure described
        in the WebServices documentation"""
        if etree.iselement(inv) is True:
            return etree.tostring(inv)
        elif type(inv) is dict:
            return xmltodict.unparse(inv)
        else:
            raise ShibaCallingError("error : bad input parameter given, expecting dict, objectify object or ElementTree element")


    @staticmethod
    def inf_constructor(shibaconnection, action, **kwargs):
        if (isinstance(shibaconnection, ShibaConnection) is False):
            raise ShibaCallingError("Internal parameter error : shibaconnection parameter is not a ShibaConnection instance")
        if action not in shibaconnection.actionsinfo:
            raise ShibaCallingError("Internal parameter error : action parameter is unknown from the actions list")
        kwargs.update(shibaconnection.actionsinfo[action])
        kwargs["action"] = action
        return kwargs

    @staticmethod
    def url_constructor(shibainit, inf):
        """URL constructor, formatting output and adding as many URL arguments as given"""
        f = ""
        pop = inf.pop("cat")
        pop2 = inf.pop("action")
        for each in inf.keys():
            if inf[each] != "" and each != "self":
                f = "%s&%s=%s" % (f, each, inf[each])
        url = "%s/%s?action=%s%s" % (shibainit.domain, pop, pop2, f)
        return url
