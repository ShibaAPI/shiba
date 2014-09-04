#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class AccountingManagement

import shiba


class AccountingManagement(shiba.Shiba):
    """Accounting Management class, showing global financial operations on your account, or specific financial details
        about an operation"""
    def __init__(self, login, pwd, domain="https://ws.priceminister.com/"):
        super(AccountingManagement, self).__init__(login, pwd, domain)
        self.url = self.domain + "wallet_ws?"

    def get_operations(self, lastoperationdate=""):
        """Get global operations which happened on your wallets, compensationid given back from XML can be used
        in the get_compensation_details method below to get more detailed information about a specific operation.
        :param lastoperationdate: as follows : dd-mm-yyyy-hh:mm:ss and as string (obviously)"""
        version = "2011-03-29"
        url = self.url + "action=getoperations" \
            + "&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + version \
            + "&operationcause=saletransfer"
        if len(lastoperationdate) > 0:
            url += "&lastoperationdate=" + str(lastoperationdate)
        dictionary = self.retrieve_dict_from_url(url)
        return dictionary

    def get_compensation_details(self, compensationid):
        """Get a specific operation details from its "compensationid" found in the get_operation request return."""
        version = "2011-03-29"
        url = self.url + "action=getcompensationdetails" \
            + "&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + version \
            + "&compensationid=" + str(compensationid)
        dictionary = self.retrieve_dict_from_url(url)
        return dictionary