#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class InventoryManagementClass

from ..shiba.shiba.Libraries.priceMinisterURLManagerClass import PriceMinisterURLManagerClass
from ..shiba.shiba.Libraries.priceMinisterXMLManagerClass import PriceMinisterXMLManagerClass
from shiba.InventoryManagement import XMLCreationClass


class InventoryManagementClass(object):
    """Les Webservices vous permettent :
    d’importer votre stock
    de vérifier l’état de vos imports
    de requêter le catalogue PriceMinister afin d’obtenir des informations sur les produits et les annonces concurrentes"""

    def __init__(self, login, pwd, version):
        self.login = login
        self.pwd = pwd
        self.version = version
        self.URLmanager = PriceMinisterURLManagerClass()
        self.XMLmanager = PriceMinisterXMLManagerClass()
        self.XMLcreation = XMLCreationClass()

    def getProductTypes(self):
        """Ce webservice sert à lire l’ensemble des types de produits PriceMinister par plate-forme. Ces types de
        produits vous serviront ensuite à obtenir l’ensemble des attributs produit pour un type défini.
        Ce webservice est accessible uniquement aux marchands profesionnels."""

        url = 'https://ws.priceminister.com/stock_ws?action=producttypes' \
              '&login='+self.login+'&pwd='+self.pwd+'&version='+self.version
        xmlresult = self.URLmanager.readPriceMinisterURL(url)
        alias_list = []

        for alias in xmlresult.findall('.//{http://pmcdn.staticpmrk.com/res/schema/genericimportfile}alias'): #TODO check ce truc
            alias_list.append(alias)

        return alias_list

    def getProductTypeTemplate(self, alias):
        """Ce Webservice sert à lire l’ensemble des attributs produit/annonce/média pour un type de produit.
        Les types de produits sont fournis grâce au Webservice précédent ProductTypes.
        Ces attributs (et les valeurs associées) servent à créer le flux XML de vos produits.
        Afin d’activer les “descriptions d’annonces personnalisées”, et les “campagnes de soldes et de promotions” sur
        votre compte, merci de contacter notre service commercial à l’adresse infopro@priceminister.com.
        Ce Webservice est accessible uniquement aux vendeurs professionnels.
        """

        attributes_list = []
        url = 'https://ws.priceminister.com/stock_ws?action=producttypetemplate&' \
              'login='+self.login+'&pwd='+self.login+'&version='+self.login+'&alias='+alias
        xmlresult = self.URLmanager.readPriceMinisterURL(url)

        for attribute in xmlresult.findall('.//{http://pmcdn.staticpmrk.com/res/schema/genericimportfile}attribute'): #TODO check ce truc
            attributes_list.append(attribute)

        return attributes_list

    def createInventoryFile(self, items):
        """Retourne le fichier xml créé pour les items.
        Afin de modifier une annonce, Vous devez indiquer l’un des 2 attributs suivant :
        SKU Vendeur: <key>sellerReference</key>
        Identifiant annonce: <key>aid</key>
        Tous les autres attributs <advert> de votre flux modifieront chacun des attributs de l’annonce.
        Ex : sellingPrice, state, comment, qty, sellerReference ...

        Afin de créer une annonce sur un produit déjà existant, vous devez indiquer tous les attributs <advert> obligatoires.
        Ensuite, le matching sur le produit se fait sur l’un des 4 attributs <product> suivants (dans l’ordre):
        Référence privée : <key>submitterreference</key> (produits de mode et maison)
        Identifiant produit PriceMinister: <key>pid</key> (tous les produits sur PriceMinister)
        Un code-barres (EAN, ISBN):<key>codebarres</key> (produits culturels)
        Référence fabricant <key>referencefabricant</key> (produits High Tech et électroménager)"""

        xmlInventory = self.XMLcreation.createImportFileXML(items)
        return xmlInventory

    def importInventoryFile(self, InventoryFile):
        """Ce Webservice permet d’envoyer des fichiers de stock (Produits / Annonces / Médias)
        sur la plateforme PriceMinister. Ce fichier doit être au format XML.
        Vous devez créer ce fichier à partir des 2 Webservices précédents.
        Ce Webservice est accessible uniquement aux vendeurs professionnels.
        IMPORTANT : Il faut transmettre le fichier d’import de stock en POST / multiPart.
        (Par exemple, en simulant l’envoi d’un formulaire HTML en POST, ou en utilisant des fonctions java,
        PHP, Curl … d’upload en MultiPart de fichiers)"""

        url = 'https://ws.priceminister.com/stock_ws?action=genericimportfile' \
              '&login='+self.login+'&pwd='+self.pwd+'&version='+self.version
        response = self.URLmanager.postPriceMinisterURL(url, InventoryFile)

        #TODO return fileid
        return response

    def exportInventory(self):
        """Ce Webservice a pour but de récupérer la liste des annonces relatives à votre inventaire.
        En outre, l’export d’inventaire donne la possibilité d’explorer les annonces concurrentes.
        Il peut donc s’avérer être un outil de repricing efficace.
        L’utilisation de ce Webservice est restreint à certains comptes utilisateurs.
        Pour bénéficier de l’export d’inventaire, merci de contacter notre service commercial à l’adresse infopro@priceminister.com."""
        #TODO
        pass

    def getAvailableShippingTypes(self):
        """Ce webservice permet de connaitre tous les modes de livraisons (classiques et personnalisés) activés par PriceMinister pour le compte marchand.
        Ce webservice est :
        accessible aux marchands professionnels ayant les droits de frais de port personnalisés activés
        et n’est pas accessible sur la plateforme espagnole"""
        #TODO
        pass

    def genericimportreport(self, fileid):
        """Ce Webservice permet de visualiser l’état de soumission de votre stock à partir du numéro « importid » fourni dans le Webservice précédent (ou visible dans : « Mon compte > Envoyer mes fichiers de stock »)
        Le fichier de stock peut être :
        -Reçu : Reçu
        -Traité : Traité
        -En attente : En attente
        -M.à.j. en cours: Import en cours
        -Annulé : Annulé
        -Aucune ligne n’a été chargée : Fichier XML corrompu
        Ce Webservice est accessible aux vendeurs professionnels uniquement."""

        url = 'https://ws.priceminister.com/stock_ws?action=genericimportreport&' \
              'login='+self.login+'&pwd='+self.pwd+'&version='+self.version+'&fileid='+fileid

        xmlresult = self.URLmanager.readPriceMinisterURL(url)
        #TODO traduire les erreurs en python
        return xmlresult
