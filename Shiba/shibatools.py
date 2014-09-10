#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class ShibaTools
# Shiba runtime tools class


from __future__ import unicode_literals

import httplib
import urllib2 as ul2
import urllib as ul

from lxml import objectify
from lxml import etree

from shibaconnection import ShibaConnection
from shibaexceptions import *

from collections import OrderedDict

import requests
import xmltodict

import pdb

"""Tools used by Shiba data retrieving classes"""
class ShibaTools(object):
    @staticmethod
    def __errors_check(obj):
        """Errors checking from the returned XML as object."""
        if "errorresponse" in obj.tag:
            if "ServerError" == obj.error.code:
                raise ShibaParameterError("Parameter error : " + obj.error.message +
                " - Reason : " + obj.error.details.detail)
            if "ParameterError" == obj.error.code:
                raise ShibaParameterError("Parameter error : " + obj.error.message +
                " - Reason : " + obj.error.details.detail)
            if "InvalidUserConnection" == obj.error.code:
                raise ShibaLoginError("Invalid user connection : " + obj.error.message +
                " - Reason : " + obj.error.details.detail)
            if "InvalidUserRights" == obj.error.code:
                raise ShibaRightsError("Invalid user rights : " + obj.error.message +
                " - Reason : " + obj.error.details.detail)
            return obj
        return False

    @staticmethod
    def post_request(url, data):
        """Method creating and submitting the multipart request of the wished to be imported XML file"""
        header = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE; rv:1.9.0.10) "
                                        "Gecko/2009042316 Firefox/3.0.10 (.NET CLR 4.0.20506)"}
        data = data.encode('utf-8')
        d = {"file": data}
        r = requests.post(url, files=d, headers=header)
        return r.text


    @staticmethod
    def retrieve_obj_from_url(url, data=None):
        """Give it an URL, will send you back a instanced object based on received XML from WebService.
        You can also give it a dict or an objectified tree to POST a file (used for import webservice)
        :rtype : lxml.objectivy class"""
        try:
            if data is not None:
                xml = ShibaTools.post_request(url, data)
            else:
                xml = ul2.urlopen(url).read()
        except requests.ConnectionError:
            raise ShibaConnectionError("HTTP error = Connection error - On URL: " + url)
        except ul2.HTTPError, e:
            raise ShibaConnectionError("HTTP error = " + unicode(e.code) + " - On URL: " + url)
        except ul2.URLError, e:
            raise ShibaConnectionError("URL error = " + unicode(e.reason) + " - On URL: " + url)
        except httplib.HTTPException:
            raise ShibaConnectionError("HTTP unknown error =" + " - On URL: " + url)
        xml = xml.decode('ISO-8859-1').encode('utf-8')
        print xml
        try:
            obj = objectify.fromstring(xml)
        except:
            raise ShibaUnknownServiceError("Unknown error from service : Service returned : " + xml)
        if ShibaTools.__errors_check(obj) is not False:
            try:
                if "Unknown error" == obj.error.code:
                    raise ShibaServiceError("Unknown error from WebService (maybe the sale isn't confirmed yet?)"
                                            " : " + obj.error.message + " - Reason : " + obj.error.details.detail)
            except ShibaServiceError:
                raise ShibaServiceError("Unknown error from WebService (maybe the sale isn't confirmed yet?)"
                                            " : " + obj.error.message + " - Reason : " + obj.error.details.detail)
            except:
                raise ShibaUnknownServiceError("An unknown error from the WebService has occurred - XML dump : " +
                                                etree.tostring(obj))
        return obj

    @staticmethod
    def create_xml_from_item_obj(inv):
        """Generate XML from the "inv" parameter, which is an object hierarchized as the XML structure described
        in the WebServices documentation"""
        if type(inv) is etree._ElementTree:
            return etree.tostring(inv)
        elif type(inv) is dict or type(inv) is OrderedDict:
            try:
                return xmltodict.unparse(inv)
            except:
                raise ShibaCallingError("error from dictionary to xml : can't create XML from dictionary, refers to xmltodict documentation"
                                        "(you don't need to add a root element 'items' to your items)")
        else:
            raise ShibaCallingError("error : bad input parameter given, expecting dict, objectify object or ElementTree element")


    @staticmethod
    def inf_constructor(shibaconnection, action, **kwargs):
        if (isinstance(shibaconnection, ShibaConnection) is False):
            raise ShibaCallingError("Internal parameter error : shibaconnection parameter is not a ShibaConnection instance")
        if action not in shibaconnection.actionsinfo:
            raise ShibaCallingError("Internal parameter error : action parameter " + action + " is unknown from the actions list")
        newkwargs = {}
        for each in kwargs:
            if kwargs[each] is not None and kwargs[each] != "":
                newkwargs[each] = kwargs[each]
        newkwargs.update(shibaconnection.actionsinfo[action])
        newkwargs["action"] = action
        return newkwargs

    @staticmethod
    def url_constructor(shibaconnection, inf, domain=None):
        """URL constructor, formatting output and adding as many URL arguments as given"""
        if domain is None:
            domain = shibaconnection.domain
        pop = inf.pop("cat")
        if "self" in inf:
            inf.pop("self")
        primary = "%s/%s?" % (domain, pop)
        url = primary + ul.urlencode(inf)
        return url
