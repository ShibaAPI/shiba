#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class AccountingManagement


from shibainit import ShibaInit
from shibatools import ShibaTools
import datetime


class AccountingManagement(ShibaInit):
    """Accounting Management class, showing global financial operations on your account, or specific financial details
        about an operation"""
    def __init__(self, login, pwd, domain="https://ws.priceminister.com/"):
        super(AccountingManagement, self).__init__(login, pwd, domain)

    def get_operations(self, lastoperationdate=""):
        """Get global operations which happened on your wallets, compensationid given back from XML can be used
        in the get_compensation_details method below to get more detailed information about a specific operation.
        :param lastoperationdate: as follows : dd/mm/yyyy-hh:mm:ss and as string or datetime"""
        operationcause = "salestransfer"
        if isinstance(lastoperationdate, datetime.datetime):
            lastoperationdate = lastoperationdate.strftime("%d/%m/%y-%H:%M:%S")
        inf = ShibaTools.inf_constructor(ShibaInit, "getoperations", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def get_compensation_details(self, compensationid):
        """Get a specific operation details from its "compensationid" found in the get_operation request return."""
        inf = ShibaTools.inf_constructor(ShibaInit, "getcompensationdetails", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj