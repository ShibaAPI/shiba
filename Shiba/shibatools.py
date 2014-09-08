#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class ShibaTools
# Shiba runtime tools class

from lxml import objectify
from lxml import etree
from shibainit import ShibaInit
import urllib2 as ul


class ShibaTools(object):
    """Tools used by Shiba data retrieving classes"""
    @staticmethod
    def retrieve_obj_from_url(url):
        """Give it an , will send you back a instanced object based on received XML from WebService.
        :rtype : lxml.objectivy class"""
        xml = ul.urlopen(url).read()
        obj = objectify.fromstring(xml)
        return obj

    @staticmethod
    def create_xml_from_item_obj(inv):
        """Generate XML from the "inv" parameter, which is an object hierarchized as the XML structure described
        in the WebServices documentation"""
        return etree.tostring(inv)

    @staticmethod
    def inf_constructor(shibainit, action, **kwargs):
        assert(isinstance(shibainit, ShibaInit)), "error : you must give a ShibaInit instance to information constructor"
        assert(action in shibainit.actionsinfo), "error : unknown action"
        cons = kwargs.update(shibainit.actionsinfo[action])
        return cons

    @staticmethod
    def url_constructor(shibainit, inf):
        """URL constructor, formatting output and adding as many URL arguments as given"""
        f = ""
        pop = inf.pop("cat")
        pop2 = inf.pop("action")
        for each in inf.keys():
            if inf[each] != "":
                f = "%s&%s=%s" % (f, each, inf[each])
        url = "%s%s%s%s" % (shibainit.domain, pop, pop2, f)
        return url
