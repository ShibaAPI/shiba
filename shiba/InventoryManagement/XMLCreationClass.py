#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class XMLCreationClass

from ..brouillons.PriceMinisterAPI.PriceMinisterAPI.Libraries.priceMinisterXMLManagerClass import PriceMinisterXMLManagerClass


class XMLCreationClass(object):
    """Permet de creeer les briques XML PriceMinister necessaires a la gestion de stock"""

    def __init__(self):
        self.XMLmanager = PriceMinisterXMLManagerClass()
        pass

    def createAttributeXML(self, key, value, unit=None):
        """Permet de creer un XML pour un attribut (key, value, (unit))"""

        xml_attribute_string = "<attribute></attribute>"
        xml_key_string = "<key>"+key+"</key>"
        xml_value_string = "<value>"+value+"</value>"

        xml_attribute = self.XMLmanager.parseXML(xml_attribute_string)
        xml_attribute.append(self.XMLmanager.parseXML(xml_key_string))
        xml_attribute.append(self.XMLmanager.parseXML(xml_value_string))

        if unit is not None:
            xml_unit_string = "<unit>"+unit+"</unit>"
            xml_attribute.append(self.XMLmanager.parseXML(xml_unit_string))

        return xml_attribute

    def createProductXML(self, attributes):
        """Permet de creer un XML pour un produit"""

        #TODO
        pass

    def createShippingtXML(self, attributes):
        """Permet de creer un XML pour un shipping"""

        #TODO
        pass

    def createAdvertXML(self, attributes):
        """Permet de creer un XML pour une annonce(advert)"""
        xml_advert_string = "<advert></advert>"
        xml_advert = self.XMLmanager.parseXML(xml_advert_string)

        # on ajoute les attributs
        for key, value, unit in attributes.iteritems(): #TODO j'ai le droit de faire ca ?
            xml_advert.append(self.createAttributeXML(key, value, unit))

        return xml_advert

    def createItemXML(self, alias, attributes):
        """Permet de crer le xml d'un item"""
        #TODO : quand il y a pas d'alias (modification d'une advert)
        #TODO : shipping balise

        xml_item_string = "<item>" \
                  "<alias>"+alias+"</alias>" \
                  "<attributes>" \
                  "</attributes>" \
                  "</item>"

        xml_item = self.XMLmanager.parseXML(xml_item_string)
        xml_item.find('attributes').append(self.createProductXML(attributes['productAttributes']))
        xml_item.find('attributes').append(self.createAdvertXML(attributes['advertAttributes']))

        return xml_item

    def createImportFileXML(self, items):
        """Permet de crer le xml pour un fichier d'import PriceMinister"""

        xml_importfile_string ="<?xml version=’1.0′ encoding=’UTF-8′?><items></items>"
        xml_importfile = self.XMLmanager.parseXML(xml_importfile_string)

        # on ajoute les items
        for alias, attributes in items.iteritems():
            xml_importfile.append(self.createItemXML(alias,attributes))

        return xml_importfile

