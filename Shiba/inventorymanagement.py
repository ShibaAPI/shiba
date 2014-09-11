#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class InventoryManagement


from __future__ import unicode_literals

from shibaconnection import ShibaConnection
from shibaexceptions import *
from shibatools import ShibaTools


class InventoryManagement(object):
    """This class permits you to manage your inventory, get information about your products and even import products
    from XML to the PriceMinister platform"""
    def __init__(self, connection):
        if isinstance(connection, ShibaConnection) is False:
            raise ShibaCallingError("Shiba subclass init error : expecting a ShibaConnection instance")
        self.connection = connection

    def product_types(self):
        """This method retrieve products types from PriceMinister, helping you to define your products attributes."""
        inf = ShibaTools.inf_constructor(self.connection, "producttypes", **locals())
        url = ShibaTools.url_constructor(self.connection, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def product_type_template(self, alias, scope=""):
        """This methods retrieve product type attributes from the product type given through the "alias" parameter.
        Dedicated to help you making your own XML import file.

        :param alias: product alias as string
        :param scope: can be either VALUES or None, VALUES as "scope" retrieve attributes values instead of only \
        attributes
        """
        inf = ShibaTools.inf_constructor(self.connection, "producttypetemplate", **locals())
        url = ShibaTools.url_constructor(self.connection, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def generic_import_report(self, fileid, nexttoken=""):
        """Retrieves the report from a previous XML import, used as verification for a proper XML import

        :param fileid: import file ID given from the generic_import_file return
        :param nexttoken: used for pagination, can be used for a loop, its precised in the return from a first call \
        to this WebService
        """
        inf = ShibaTools.inf_constructor(self.connection, "genericimportreport", **locals())
        url = ShibaTools.url_constructor(self.connection, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def generic_import_file(self, data):
        """Import XML file to your PriceMinister inventory trough a POST request.

        :param data: must be a object/dict (OrderedDict is better) containing your inventory wished to be imported. \
        You must respect the XML hierarchy detailed from the WebService documentation inside the object/dict
        """
        data = ShibaTools.create_xml_from_item_obj(data)
        inf = ShibaTools.inf_constructor(self.connection, "genericimportfile")
        url = ShibaTools.url_constructor(self.connection, inf)
        obj = ShibaTools.retrieve_obj_from_url(url, data)
        return obj

    def get_available_shipping_types(self):
        """Retrieves available shipping options at asking time"""
        inf = ShibaTools.inf_constructor(self.connection, "getavailableshippingtypes", **locals())
        url = ShibaTools.url_constructor(self.connection, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def export_inventory(self, scope="", nexttoken=""):
        """Export adverts from your inventory, nexttoken pagination is available.

        :param scope: PRICING is the only acceptable value for it, if not empty."""
        inf = ShibaTools.inf_constructor(self.connection, "export", **locals())
        url = ShibaTools.url_constructor(self.connection, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj
