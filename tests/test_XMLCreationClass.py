#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_XMLCreationClass
# permet de tester unitairement la classe XMLCreationClass

from nose.tools import *

from ..shiba.shiba.InventoryManagement.XMLCreationClass import XMLCreationClass
from ..brouillons.shiba.shiba.Libraries.priceMinisterXMLManagerClass import PriceMinisterXMLManagerClass


class test_XMLCreationClass(unittest.TestCase):

    def test_createAttributeXML_1(self):
        """ttest de la generation xml createAttributeXML"""

        XMLmanagement = PriceMinisterXMLManagerClass()
        key = 'sellingPrice'
        value = 35
        xmlcreation = XMLCreationClass()
        xmlresult = xmlcreation.createAttributeXML(key, value)

        xmltest_string = "<attribute>" \
                  "<key>sellingPrice</key>" \
                  "<value>35</value>" \
                  "</attribute>"

        xmltest = XMLmanagement.parseXML(xmltest_string)

        self.assertTrue(xmlresult == xmltest)

    def test_createAdvertXML_1(self):
        """test de la generation xml createAdvertItem"""

        XMLmanagement = PriceMinisterXMLManagerClass()
        attributes = {
            'sellingPrice': 35,
            'state': 15,
            'comment': 'super article!',
            'qty': 3,
            'sellerReference': 'Nous meme',
        }

        xmlcreation = XMLCreationClass()
        xmlresult = xmlcreation.createAdvertXML(attributes)

        xmltest_string = "<item>" \
                  "<alias>alias12345</alias>" \
                  "<attributes>" \
                  "<product>" \
                  "<attribute>" \
                  "<key>sellerReference</key>" \
                  "<value>SKU12345SKU_1234567890</value>" \
                  "</attribute>" \
                  "<attribute>" \
                  "<key>aid</key>" \
                  "<value>aid12345</value>" \
                  "</attribute>" \
                  "</product>" \
                  "<advert>" \
                  "<attribute>" \
                  "<key>sellingPrice</key>" \
                  "<value>35</value>" \
                  "</attribute>" \
                  "<attribute>" \
                  "<key>state</key>" \
                  "<value>15</value>" \
                  "</attribute>" \
                  "<attribute>" \
                  "<key>comment</key>" \
                  "<value>super article!</value>" \
                  "</attribute>" \
                  "<attribute>" \
                  "<key>qty</key>" \
                  "<value>3</value>" \
                  "</attribute>" \
                  "<attribute>" \
                  "<key>sellerReference</key>" \
                  "<value>Nous meme</value>" \
                  "</attribute>" \
                  "</advert>" \
                  "</attributes>" \
                  "</item>"

        xmltest = XMLmanagement.parseXML(xmltest_string)

        self.assertTrue(xmlresult == xmltest)

    def test_createItemXML_1(self):
        """test de la generation xml createItemXML"""

        XMLmanagement = PriceMinisterXMLManagerClass()
        alias = 'alias12345'
        attributes = {
            'productattributes': {
                'codebarres': 'EAN1234567890',
                'pid': 'PID1234567890',
            },
            'advertattributes': {
                'sellerReference': 'SKU12345SKU_1234567890',
                'sellingPrice': 35,
                'state': 15,
                'comment': 'super article!',
                'qty': 3,
            },
        }

        xmlcreation = XMLCreationClass()
        xmlresult = xmlcreation.createItemXML(alias, attributes)

        xmltest_string = "<item>" \
                  "<attributes>" \
                  "<product>" \
                  "<attribute>" \
                  "<key>codebarres</key>" \
                  "<value>EAN1234567890</value>" \
                  "</attribute>" \
                  "<attribute>" \
                  "<key>pid</key>" \
                  "<value>PID1234567890</value>" \
                  "</attribute>" \
                  "</product>" \
                  "<advert>" \
                  "<attribute>" \
                  "<key>sellerReference</key>" \
                  "<value>SKU12345SKU_1234567890</value>" \
                  "</attribute>" \
                  "<attribute>" \
                  "<key>sellingPrice</key>" \
                  "<value>35</value>" \
                  "</attribute>" \
                  "<attribute>" \
                  "<key>state</key>" \
                  "<value>15</value>" \
                  "</attribute>" \
                  "<attribute>" \
                  "<key>comment</key>" \
                  "<value>super article!</value>" \
                  "</attribute>" \
                  "<attribute>" \
                  "<key>qty</key>" \
                  "<value>3</value>" \
                  "</attribute>" \
                  "</advert>" \
                  "</attributes>" \
                  "</item>"

        xmltest = XMLmanagement.parseXML(xmltest_string)

        self.assertTrue(xmlresult == xmltest)

    def test_createImportFileXML_1(self):
        """test de la generation xml createImportFileXML"""

        XMLmanagement = PriceMinisterXMLManagerClass()
        alias = 'alias12345'
        attributes = {
            'productattributes': {
                'codebarres': 'EAN1234567890',
                'pid': 'PID1234567890',
            },
            'advertattributes': {
                'sellerReference': 'SKU12345SKU_1234567890',
                'sellingPrice': 35,
                'state': 15,
                'comment': 'super article!',
                'qty': 3,
            },
        }

        xmlcreation = XMLCreationClass()
        xmlresult = xmlcreation.createItemXML(alias, attributes)

        xmltest_string = "<?xml version=’1.0′ encoding=’UTF-8′?>" \
                         "<items>" \
                         "<item>" \
                         "<attributes>" \
                         "<product>" \
                         "<attribute>" \
                         "<key>codebarres</key>" \
                         "<value>EAN1234567890</value>" \
                         "</attribute>" \
                         "<attribute>" \
                         "<key>pid</key>" \
                         "<value>PID1234567890</value>" \
                         "</attribute>" \
                         "</product>" \
                         "<advert>" \
                         "<attribute>" \
                         "<key>sellerReference</key>" \
                         "<value>SKU12345SKU_1234567890</value>" \
                         "</attribute>" \
                         "<attribute>" \
                         "<key>sellingPrice</key>" \
                         "<value>35</value>" \
                         "</attribute>" \
                         "<attribute>" \
                         "<key>state</key>" \
                         "<value>15</value>" \
                         "</attribute>" \
                         "<attribute>" \
                         "<key>comment</key>" \
                         "<value>super article!</value>" \
                         "</attribute>" \
                         "<attribute>" \
                         "<key>qty</key>" \
                         "<value>3</value>" \
                         "</attribute>" \
                         "</advert>" \
                         "</attributes>" \
                         "</item>" \
                         "<item>" \
                         "<attributes>" \
                         "<product>" \
                         "<attribute>" \
                         "<key>codebarres</key>" \
                         "<value>EAN1234567890</value>" \
                         "</attribute>" \
                         "<attribute>" \
                         "<key>pid</key>" \
                         "<value>PID1234567890</value>" \
                         "</attribute>" \
                         "</product>" \
                         "<advert>" \
                         "<attribute>" \
                         "<key>sellerReference</key>" \
                         "<value>SKU12345SKU_1234567890</value>" \
                         "</attribute>" \
                         "<attribute>" \
                         "<key>sellingPrice</key>" \
                         "<value>35</value>" \
                         "</attribute>" \
                         "<attribute>" \
                         "<key>state</key>" \
                         "<value>15</value>" \
                         "</attribute>" \
                         "<attribute>" \
                         "<key>comment</key>" \
                         "<value>super article!</value>" \
                         "</attribute>" \
                         "<attribute>" \
                         "<key>qty</key>" \
                         "<value>3</value>" \
                         "</attribute>" \
                         "</advert>" \
                         "</attributes>" \
                         "</item>" \
                         "</items>"

        xmltest = XMLmanagement.parseXML(xmltest_string)

        self.assertTrue(xmlresult == xmltest)




