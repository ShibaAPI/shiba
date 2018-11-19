# -*- coding: utf-8 -*-
""" Tools used by Shiba data retrieving classes"""
from __future__ import unicode_literals

import re
from collections import OrderedDict

import requests
import xmltodict

from furl import furl
from lxml import etree
from lxml import objectify
from lxml.etree import XMLSyntaxError

from ftfy import fix_text

from .shibaconnection import ShibaConnection
from .shibaresponseobject import ShibaResponseObject
from .shibaexceptions import (ShibaParameterError, ShibaLoginError, ShibaQuotaExceededError,
                              ShibaRightsError, ShibaConnectionError, ShibaUnknownServiceError, ShibaServiceError,
                              ShibaCallingError)

from http.client import HTTPException


def post_request(url, data):
    """Method creating and submitting the multipart request of the wished to be imported XML file.

    :param data: raw XML as text

    :rtype: plain text from servers response
    """
    header = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE; rv:1.9.0.10) "
                            "Gecko/2009042316 Firefox/3.0.10 (.NET CLR 4.0.20506)"}
    d = {"file": data}
    r = requests.post(url, files=d, headers=header)
    return r.text


def retrieve_obj_from_url(url, data=None):
    """Give it an URL, will send you back an object based on received XML from WebService, it removes and store
    namespace as its not really useful for common usages of this API.
    You can also give it a dict or an objectified tree to POST a file (used for import webservice)
    :param url: fully formatted URL from url_constructor
    :param data: if not None, will send a POST request to URL instead of a GET one, with multipart sending of
    this parameter content

    :rtype : ShibaResponseObject object, containing lxml.objectify class, raw XML as Unicode string and the
    namespace from the XML.
    """
    try:
        if data is not None:
            xml = post_request(url, data)
        else:
            xml = requests.get(url).text
    except requests.ConnectionError:
        raise ShibaConnectionError("HTTP error = Connection error - On URL: " + url)
    except requests.HTTPError as e:
        raise ShibaConnectionError("URL error = " + e.reason + " - On URL: " + url)
    except HTTPException:
        raise ShibaConnectionError("HTTP unknown error =" + " - On URL: " + url)

    namespace = re.search(pattern='xmlns="[^"]', string=xml)
    if namespace is not None:
        namespace = namespace.group()
    else:
        namespace = ""

    xmlepured = re.sub(pattern=' xmlns="[^"]+"', repl='', string=xml, flags=0)
    xmlepured = fix_text(xmlepured).encode('utf-8')

    try:
        obj = objectify.fromstring(xmlepured)
    except XMLSyntaxError:
        print(xmlepured)
        raise

    if _check_errors(obj) is not False:
        try:
            if "Unknown error" == obj.error.code:
                raise ShibaServiceError("Unknown error from WebService (maybe the sale isn't confirmed yet?)"
                                        " : " + obj.error.message + " - Reason : " + obj.error.details.detail)
        except ShibaServiceError:
            raise ShibaServiceError("Unknown error from WebService (maybe the sale isn't confirmed yet?)"
                                    " : " + obj.error.message + " - Reason : " + obj.error.details.detail)
        except Exception:
            raise ShibaUnknownServiceError("An unknown error from the WebService has occurred - XML dump : " +
                                           etree.tostring(obj))
    return ShibaResponseObject(namespace, obj, xml.encode('utf-8'))


def create_xml_from_item_obj(inv):
    """Generate XML from the "inv" parameter.

    :param inv: is an object or a dict hierarchized as the XML structure described \
    in the WebServices documentation. Take a look at the xmltodict or the lxml.objectify documentation too.

    :rtype: string output from objectified element or ElementTree element tostring() methods
    """
    if type(inv) is etree._ElementTree:
        return etree.tostring(inv)
    elif type(inv) is dict or type(inv) is OrderedDict:
        try:
            return xmltodict.unparse(inv)
        except Exception:
            raise ShibaCallingError("error from dictionary to xml : can't create XML from dictionary,"
                                    " refers to xmltodict documentation"
                                    "(you don't need to add a root element 'items' to your items)")
    else:
        raise ShibaCallingError("error : bad input parameter given, "
                                "expecting dict, objectify object or ElementTree element")


def inf_constructor(shibaconnection, action, **kwargs):
    """Just a selective concatenation of args given and related static data from the given action.

    :param shibaconnection: ShibaConnection class instance
    :param action: string giving the action type for the WebService
    :param kwargs: params to concatenate

    :rtype epured and updated dict
    """
    if isinstance(shibaconnection, ShibaConnection) is False:
        raise ShibaCallingError("Internal parameter error : shibaconnection parameter is not "
                                "a ShibaConnection instance")
    if action not in shibaconnection.actionsinfo:
        raise ShibaCallingError("Internal parameter error : action parameter " +
                                action + " is unknown from the actions list")
    newkwargs = {}
    for each in kwargs:
        if kwargs[each] is not None and kwargs[each] != "":
            newkwargs[each] = kwargs[each]
    newkwargs.update(shibaconnection.actionsinfo[action])
    newkwargs["action"] = action
    return newkwargs


def url_constructor(shibaconnection, params, domain=None):
    """URL constructor, formatting input and adding as many URL arguments as given.

    :param params: info dict, from inf_constructor
    :param domain: force URL domain, useful for some actions needing to go with http instead of https

    :rtype: formatted URL string
    """
    params.pop("self", None)
    category = params.pop("cat")
    ordered_params = OrderedDict(((k, params[k]) for k in sorted([k for k in params])))

    f = furl(domain or shibaconnection.domain)
    f.path.segments.append(category)
    f.path.normalize()
    f.add(ordered_params)
    return f.url


def _check_errors(obj):
    """Errors checking from the returned XML as object. Handling errors as internal exceptions raising

    :param obj: objectified element to check errors from

    :rtype: objectified element if errors have been found, False if the WebService hasn't encountered an error
    """
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
            if "Quota exceeded" in obj.error.message.text:
                raise ShibaQuotaExceededError("Too many requests : " + obj.error.message +
                                              " - Reason : " + obj.error.details.detail)
            else:
                raise ShibaRightsError("Invalid user rights : " + obj.error.message +
                                       " - Reason : " + obj.error.details.detail)
        return obj
    return False
