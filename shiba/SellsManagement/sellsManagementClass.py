#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class sellsManagementClass

from ..shiba.shiba.Libraries.priceMinisterURLManagerClass import PriceMinisterURLManagerClass
from ..shiba.shiba.Libraries.priceMinisterXMLManagerClass import PriceMinisterXMLManagerClass

class SellsManagementClass(object):
    """Cet ensemble de Webservices vous permet d’automatiser ou d’interfacer avec votre SI la gestion des nouvelles ventes :
    listing des nouvelles ventes
    confirmation des ventes
    récupération des informations permettant l’envoi du colis."""

    def __init__(self, login, pwd, version):
        self.login = login
        self.pwd = pwd
        self.version = version
        self.URLmanager = PriceMinisterURLManagerClass()
        self.XMLmanager = PriceMinisterXMLManagerClass()

    def getnewsales(self):
        """Ce Webservice permet de récupérer la liste des nouvelles ventes (ventes à confirmer).
        Il est accessible à la fois aux vendeurs particuliers et aux marchands pro.
        Cependant, les particuliers n’auront pas accès aux données relatives aux coordonnées de l’acheteur
        (pour cela ils devront tout d’abord confirmer la vente puis invoquer le WS getshippinginformation)"""

        url = 'https://ws.priceminister.com/sales_ws?action=getnewsales&login='+self.login+'&pwd='+self.pwd+'&version='+self.version
        xmlresult = self.URLmanager.readPriceMinisterURL(url)
        itemid_list = []

        for itemid in xmlresult.findall('.//{http://pmcdn.staticpmrk.com/res/schema/genericimportfile}item'):
            itemid_list.append(itemid)

        return itemid_list, xmlresult

    def acceptsale(self, itemid):
        """Ce Webservice permet d’accepter ou de refuser les nouvelles ventes (ventes à confirmer) reçues avec le précédent Webservice.
        Il est accessible à la fois aux vendeurs particuliers et aux vendeurs professionnels."""

        url = 'https://ws.priceminister.com/sales_ws?action=acceptsale&login='+self.login+'&pwd='+self.pwd+'&version='+self.version+'&itemid='+itemid
        xmlresult = self.URLmanager.readPriceMinisterURL(url)

        return xmlresult

    def refusesale(self, itemid):
        """Ce Webservice permet d’accepter ou de refuser les nouvelles ventes (ventes à confirmer) reçues avec le précédent Webservice.
        Il est accessible à la fois aux vendeurs particuliers et aux vendeurs professionnels."""

        url = 'https://ws.priceminister.com/sales_ws?action=refusesale&login='+self.login+'&pwd='+self.pwd+'&version='+self.version+'&itemid='+itemid
        xmlresult = self.URLmanager.readPriceMinisterURL(url)

        return xmlresult