from .. import shiba


class SalesManagement(shiba.Shiba):
    """Primary sales management class, gather all sales-related methods"""

    def __init__(self, login, pwd, version):
        self.nexttoken = 0
        super(SalesManagement, self).__init__(login, pwd, version)

    def get_new_sales(self):
        """Calling get_new_sales method gives you back a dictionnary from returned XML"""
        url = self.url + "action=getnewsales&login=" + self.login \
              + "&pwd=" + self.pwd \
              + "&version=" + self.version
        namespace = "http://pmcdn.priceminister.com/res/schema/getnewsales"
        dictionary = self.__retrieve_dict_from_url(url, namespace)
        return dictionary

    def sale_action(self, itemid, action):
        """Accept/Refuse sale, give your answer as third argument ("refuse", "accept")"""
        assert (str(action) == "refusesale" or str(action) == "acceptsale"), "error : invalid action given"
        url = self.url + "action=" + str(action) + "&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version \
            + "&itemid=" + str(itemid)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/saleacceptance")
        return dictionary

    def get_current_sales(self, prepurchase=False, datefrom="", next=self.nexttoken):
        """Calling get_current_sales method gives you a dictionary gathering all current sales
        param: prepurchase: Boolean which on True gives you the list of preordered sales
        param: datefrom: Formatted as "yyyy-mm-dd" string allows you to filter the sales only from the given date
        param: next: Next page token argument, leave at is it, only give 0 is you want the first page"""
        url = self.url + "action=getcurrentsales&login=" + self.login \
              + "&pwd=" + self.pwd \
              + "&version=" + self.version
        if prepurchase is not False:
            url += "&ispendingorder=y"
        if len(datefrom) != 0:
            url += "&purchasedate=" + str(datefrom)
        if next != 0 and self.nexttoken != 0:
            url += "&nexttoken=" + str(self.nexttoken)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/getcurrentsales")
        self.nexttoken = self.__get_next_token(dictionary)
        return dictionary

    def get_billing_information(self, purchaseid):
        """Calling this method gives you accounting informations about a confirmed order.
        param: purchaseid: is mandatory"""
        purchaseid = str(purchaseid)
        url = self.url + "action=getbillinginformation&login=" + self.login\
              + "&pwd=" + self.pwd \
              + "&version=" + self.version\
              + "purchaseid=" + purchaseid
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/getbillinginformation")
        return dictionary