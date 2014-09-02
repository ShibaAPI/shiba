from .. import shiba


class SalesManagement(shiba.ShibaMain):
    """#Primary sales management class, gather all sales-related methods"""

    def __init__(self, login, pwd, version):
        super(SalesManagement, self).__init__(login, pwd, version)

    def get_new_sales(self):
        """#Calling getNewSales method gives you back a dictionnary from returned XML"""
        url = "https://ws.priceminister.com/sales_ws?action=getnewsales&login=" + self.login \
              + "&pwd=" + self.pwd \
              + "&version=" + self.version
        namespace = "http://pmcdn.priceminister.com/res/schema/getnewsales"
        dictionary = self.retrieve_dict_from_url(url, namespace)
        return dictionary

    def sale_action(self, itemid, action):
        """Accept/Refuse sale, give your answer as third argument ("refuse", "accept")"""
        assert (str(action) == "refuse" or str(action) == "accept"), "error : invalid action given"
        url = "https://ws.priceminister.com/sales_ws?action=" + str(action) + "sale&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version \
            + "&itemid=" + str(itemid)
        dictionary = self.retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/saleacceptance")
        return dictionary