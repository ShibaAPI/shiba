#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class PricesforAsinListClass


class PricesforAsinListClass(object):
    """Ce webservice permet de récupérer une liste de produits à partir d’une recherche sur :
    Des mots-clés
    Des noms de catégories
    #Un ou une liste d’ID_produit (référence produit PriceMinister)
    Un ou une liste de références (EAN, ISBN)
    Le résultat de ce Webservice est une liste de produits avec des informations :
    Produit : titre, image, url, auteur …
    Offre : le meilleur Prix neuf et le meilleur prix occasion, les 10 premières annonces neuves et occasions"""

    def __init__(self, login, pwd, version):
        self.url = 'https://ws.priceminister.com/stock_ws?action=export&login=xxxxxxx&pwd=xxxxxxx&version=xxxx-xx-xx'

    def getPricesforAsinList(self, plateforme_id, sens, account_id):
        pass


