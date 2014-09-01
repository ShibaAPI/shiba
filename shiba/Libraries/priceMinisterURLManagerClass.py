#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class PriceMinisterURLReaderClass

import urllib2 as UL
import xml.etree.cElementTree as ET


class PriceMinisterURLManagerClass(object):
    """Permet de :
    _recevoir le flux XML des web services de PriceMinister
    _poster un fichier XML a une URL
    """
    #TODO convertir les xxxx generaux des url avec pwd login etc

    def __init__(self):
        pass

    def readPriceMinisterURL(self, url):
        try:
            f = UL.urlopen(url)
            xmlresult = f.read()
            root = ET.fromstring(xmlresult)
        except:
            raise

        return root

    def postPriceMinisterURL(self, url, data):
        try:
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            header = { 'User-Agent' : user_agent }
            req = UL.Request(url, data, header)  # POST request doesn't not work
            response = UL.urlopen(req)
        except:
            raise

        return response