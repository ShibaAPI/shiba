#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class AccountingClass


class AccountingClass(object):
    """Ce webservice permet de récupérer les opérations financières ayant eu lieu sur votre porte monnaie virtuel.
    Le nombre de résultats maximum retournés est de 200 opérations et un système de pagination a été mis en place pour vous permettre de récupérer des opérations selon une date donnée.
    Ce WS est accessible aux marchands professionnels et aux vendeurs particuliers."""

    def __init__(self, login, pwd, version):
        self.login = login
        self.pwd = pwd
        self.version = version

    def GetOperations(self):
        """Ce webservice permet de récupérer les opérations financières ayant eu lieu sur votre porte monnaie virtuel.
        Le nombre de résultats maximum retournés est de 200 opérations et un système de pagination a été mis en place pour vous permettre de récupérer des opérations selon une date donnée.
        Ce WS est accessible aux marchands professionnels et aux vendeurs particuliers."""

        url = 'https://ws.priceminister.com/stock_ws?action=genericimportfile&' \
              'login='+self.login+'&pwd='+self.pwd+'&version='+self.version
        pass

    def GetCompensationDetails(self):
        """Ce webservice permet de récupérer le détail d’une opération financière donnée via son numéro de compensation.
        Dans le cas d’une opération de type « salestransfer » vous retrouverez la liste des articles qui vous ont été payés
        ainsi que d’autres données de type comptable (abonnement mensuel, ventes annulées, remboursement des frais de port, etc…).
        Ce webservice ne récupère que les éléments de facturations relatifs aux articles vendus. Il ne retourne pas les gestes ou pénalités commerciales.
        Ce webservice est accessible uniquement aux marchands professionnels."""

        url = 'https://ws.priceminister.com/sales_ws?action=getcompensationdetails&' \
              'login='+self.login+'&pwd='+self.pwd+'&version='+self.version+'&compensationid=xxxxx'
