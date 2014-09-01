#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class PriceMinisterAPIClass

from shiba.Libraries.priceMinisterURLManagerClass import PriceMinisterURLManagerClass
from shiba.InventoryManagement.inventoryManagementClass import InventoryManagementClass
from shiba.SellsManagement.sellsManagementClass import SellsManagementClass


class PriceMinisterAPIClass(object):
    """Nous distinguons 4 types de Webservices :
    Gestion du stock
    _Ces Webservices permettent au vendeur :
    _De requêter le catalogue PriceMinister afin d’obtenir des informations sur les produits et les annonces concurrentes
    _D’importer son stock
    _De vérifier l’état de cet import
    Nouvelles ventes
    _Cet ensemble de Webservices permet au vendeur d’automatiser ou d’interfacer avec son SI la gestion des nouvelles ventes : listing des nouvelles ventes, confirmation/refus des ventes, etc.
    Actions post acceptation de vente
    _L’ensemble de ces Webservices permet la gestion des articles et la relation avec l’acheteur après la confirmation complète de la vente :
    _Récupération des éléments relatifs à l’expédition de la commande
    _Correspondance avec l’acheteur (envoi d’informations sur l’expédition de la commande, réception de questions de l’acheteur, etc.)
    _Correspondance avec PriceMinister
    _Traitement d’une réclamation
    Comptabilité
    _Ces Webservices vous permettront de récupérer via WS la liste et le détail des opérations financières effectuées sur votre Porte-Monnaie virtuel."""

    def __init__(self, login, pwd, version):
        self.login = login
        self.pwd = pwd
        self.version = version
        self.urlreader = PriceMinisterURLManagerClass()
        self.inventoryManagement = InventoryManagementClass(login, pwd, version)
        self.sellsManagement = SellsManagementClass(login, pwd, version)

    def addProductsToInventory(self, items):
        """quelle forme pour les items??
        un dictionnaire
        cle : 'alias', valeur : 'Attributes' {productAttributes, advertAttributes, shippingAttributes}
        alias = 'alias12345'
        productattributes = {
            'codebarres': 'EAN1234567890',
            'pid': 'PID1234567890',
        }
        advertattributes = {
            'sellerReference': 'SKU12345SKU_1234567890',
            'sellingPrice': 35,
            'state': 15,
            'comment': 'super article!',
            'qty': 3,
        }
        """

        xmlfile = self.inventoryManagement.createInventoryFile(items)
        self.inventoryManagement.importInventoryFile(xmlfile)
        #TODO on checke l'etat de traitment du fichier ?
        pass

    def updatePricesForProducts(self, items):
        """quelle forme pour les items??"""
        #TODO si on veut update que les prix ?
        pass

    def getOrders(self):
        """permet de recuperer les commandes en cours"""

        itemid_list, xmlresult = self.sellsManagement.getnewsales()
        return itemid_list, xmlresult

    def acceptOrder(self, itemid):
        """permet d'accepter une commande"""

        response = self.sellsManagement.acceptsale(itemid)
        return response

    def refuseOrder(self, itemid):
        """permet de refuser une commande"""

        response = self.sellsManagement.refusesale(itemid)
        return response
