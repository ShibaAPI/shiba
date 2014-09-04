#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class InventoryManagement

from .. import shiba
import urllib2 as ul

class InventoryManagement(shiba.Shiba):
    """This class permits you to manage your inventory, get informations about your products and even import products
    from XML to the PriceMinister platform"""
    def __init__(self, login, pwd, version, domain="https://ws.priceminister.com/"):
        super(InventoryManagement, self).__init__(login, pwd, version, domain)
        self.url = self.domain + "stock_ws?"

    def product_types(self):
        """This method retrieve products types from PriceMinister, helping you to define your products attributes."""
        url = self.url + "action=producttypes" \
            + "&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/stock_ws/producttypes")
        return dictionary

    def product_type_template(self, alias, scope=""):
        """This methods retrieve product type attributes from the product type given through the "alias" parameter.
            Dedicated to help you making your own XML import file.
            Param "scope" can be either VALUES or None, VALUES as "scope" retrieve attributes values instead of only
            attributes"""
        url = self.url + "action=producttypetemplate" \
            + "&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version \
            + "&alias=" + str(alias)
        if len(scope) > 0:
            url += "&scope=" + str(scope)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/stock_ws/producttypetemplate")
        return dictionary

    def generic_import_report(self, fileid, nexttoken=0):
        """Retrieves the report from a previous XML import, used as verification for a proper XML import"""
        url = self.url + "action=genericimportreport" \
            + "&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version \
            + "&fileid=" + str(fileid)
        if nexttoken != 0:
            url += "&nexttoken=" + str(nexttoken)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/stock_ws/genericimportreport")
        return dictionary

    def generic_import_file(self, data):
        """Import XML file to your PriceMinister inventory trough a POST request.
        "data" parameter must be a dictionary containing your inventory wished to be imported. You must respect the XML
        hierarchy detailed from the WebService documentation inside the dictionary"""
        url = self.url + "action=genericimportfile" \
            + "&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version
        file = self.__create_xml_from_item_dict(data)
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        hea = {"User-Agent" : user_agent}
        req = ul.Request(url, file, hea)
        dictionary = self.__retrieve_dict_from_url(req, "http://www.priceminister.com/stock_ws/genericimportfile")
        return dictionary