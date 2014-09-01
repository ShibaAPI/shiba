#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class PriceMinisterXMLReaderClass

import xml.etree.cElementTree as ET


class PriceMinisterXMLManagerClass(object):
    """Librairie de manipulation XML"""

    def __init__(self):
        pass

    def parseXML(self, string):
        """Permet de parser un fichier xml a partir d un fichier/string"""

        try:
            parsed = ET.parse(string)
        except:
            raise

        return parsed