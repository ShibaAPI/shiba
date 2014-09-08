#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class InventoryManagement

from shibainit import ShibaInit
import urllib2 as ul
from shibatools import ShibaTools


class InventoryManagement(ShibaInit):
    """This class permits you to manage your inventory, get informations about your products and even import products
    from XML to the PriceMinister platform"""
    def __init__(self, login, pwd, domain="https://ws.priceminister.com/"):
        super(InventoryManagement, self).__init__(login, pwd, domain)

    def product_types(self):
        """This method retrieve products types from PriceMinister, helping you to define your products attributes."""
        inf = ShibaTools.inf_constructor(ShibaInit, "producttypes", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def product_type_template(self, alias, scope=""):
        """This methods retrieve product type attributes from the product type given through the "alias" parameter.
        Dedicated to help you making your own XML import file.
        Param "scope" can be either VALUES or None, VALUES as "scope" retrieve attributes values instead of only
        attributes"""
        inf = ShibaTools.inf_constructor(ShibaInit, "producttypetemplate", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def generic_import_report(self, fileid, nexttoken=""):
        """Retrieves the report from a previous XML import, used as verification for a proper XML import"""
        inf = ShibaTools.inf_constructor(ShibaInit, "genericimportreport", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def generic_import_file(self, data):
        """Import XML file to your PriceMinister inventory trough a POST request.
        "data" parameter must be a obj containing your inventory wished to be imported. You must respect the XML
        hierarchy detailed from the WebService documentation inside the obj"""
        inf = ShibaTools.inf_constructor(ShibaInit, "genericimportfile")
        url = ShibaTools.url_constructor(ShibaInit, inf)
        retfile = ShibaTools.create_xml_from_item_obj(data)
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        hea = {"User-Agent": user_agent}
        req = ul.Request(url, retfile, hea)
        obj = ShibaTools.retrieve_obj_from_url(req)
        return obj

    def get_available_shipping_types(self):
        """Retrieves available shipping at asking time"""
        inf = ShibaTools.inf_constructor(ShibaInit, "getavailableshippingtypes", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def export_inventory(self, scope="", nexttoken=""):
        """Export adverts from your inventory, nexttoken pagination is available"""
        inf = ShibaTools.inf_constructor(ShibaInit, "cancelitem", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj