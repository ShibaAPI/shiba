__author__ = "boguta_m"

from .. import shiba


class AccountingManagement(shiba.Shiba):
    """Accounting Management class, showing global financial operations on your account, or specific financial details
        about an operation"""
    def __init__(self, login, pwd, version, mode=""):
        if mode is "test":
            self.url = "https://ws.sandbox.priceminister.com/wallet_ws?"
        else:
            self.url = "https://ws.priceminister.com/wallet_ws?"
        super(AccountingManagement, self).__init__(login, pwd, version, mode)

    def get_operations(self, lastoperationdate=""):
        """Get global operations which happened on your wallets, compensationid given back from XML can be used
        in the get_compensation_details method below to get more detailed information about a specific operation.
        :param lastoperationdate: as follows : dd-mm-yyyy-hh:mm:ss and as string (obviously)"""
        url = self.url + "action=getoperations" \
            + "&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version \
            + "&operationcause=saletransfer"
        if len(lastoperationdate) > 0:
            url += "&lastoperationdate=" + str(lastoperationdate)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/wallet_ws/getoperations")
        return dictionary

    def get_compensation_details(self, compensationid):
        """Get a specific operation details from its "compensationid" found in the get_operation request return."""
        url = self.url + "action=getcompensationdetails" \
            + "&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version \
            + "&compensationid=" + str(compensationid)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/wallet_ws/getcompensationdetails")
        return dictionary