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
                " Reason : " + obj.error.details.detail)
            if "ParameterError" == obj.error.code:
                raise ShibaParameterError("Parameter error : " + obj.error.message +
                " Reason : " + obj.error.details.detail)
            if "InvalidUserConnection" == obj.error.code:
                raise ShibaLoginError("Invalid user connection : " + obj.errorresponse.error.message +
                " Reason : " + obj.error.details.detail)
            return True
        return False

    @staticmethod
    def retrieve_obj_from_url(url, data=None):
        """Give it an URL, will send you back a instanced object based on received XML from WebService.
        You can also give it a dict or an objectified tree to POST a file (used for import webservice)
        :rtype : lxml.objectivy class"""
        try:
            if data is not None:
                header = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10 (.NET CLR 4.0.20506)"}
                data = data.encode('utf-8')
                d = ul.quote_plus(data)
                d = {"file": d}
                r = requests.post(url, files=d, headers=header)
                xml = str(r.text)
            else:
                xml = ul2.urlopen(url).read()
        except ul2.HTTPError, e:
            raise ShibaConnectionError("HTTP error = " + unicode(e.code) + " - On URL: " + url)
        except ul2.URLError, e:
            raise ShibaConnectionError("URL error = " + unicode(e.reason) + " - On URL: " + url)
        except httplib.HTTPException:
            raise ShibaConnectionError("HTTP unknown error =" + " - On URL: " + url)
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
            try:
                return xmltodict.unparse({"items": inv})
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
            raise ShibaCallingError("Internal parameter error : action parameter is unknown from the actions list")
        kwargs.update(shibaconnection.actionsinfo[action])
        kwargs["action"] = action
        return kwargs

    @staticmethod
    def url_constructor(shibainit, inf):
        """URL constructor, formatting output and adding as many URL arguments as given"""
        pop = inf.pop("cat")
        if "self" in inf:
            inf.pop("self")
        primary = "%s/%s?" % (shibainit.domain, pop)
        url = primary + ul.urlencode(inf)
        return url
