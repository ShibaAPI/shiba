__author__ = "boguta_m"

from .. import shiba


class SalesManagement(shiba.Shiba):
    """Primary sales management class, gather all sales-related methods. Those methods returns a dictionary
    from the XML given as answer by the related WebService."""

    def __init__(self, login, pwd, version, mode=""):
        self.nexttoken = 0
        super(SalesManagement, self).__init__(login, pwd, version, mode)

    def get_new_sales(self):
        """Calling get_new_sales method gives you back a dictionary from returned XML, featuring all the new sales which
        have been done."""
        url = self.url + "action=getnewsales&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version
        namespace = "http://pmcdn.priceminister.com/res/schema/getnewsales"
        dictionary = self.__retrieve_dict_from_url(url, namespace)
        return dictionary

    def sale_action(self, itemid, action):
        """Accept/Refuse sale, give your answer as third argument ("refuse", "accept")."""
        assert (str(action) == "refusesale" or str(action) == "acceptsale"), "error : invalid action given"
        url = self.url + "action=" + str(action) \
            + "&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version \
            + "&itemid=" + str(itemid)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/saleacceptance")
        return dictionary

    def get_current_sales(self, prepurchase=False, datefrom="", token=-1):
        """Calling get_current_sales method gives you a dictionary gathering all current sales.
        :param prepurchase: Boolean which on True gives you the list of preordered sales
        :param datefrom: Formatted as "yyyy-mm-dd" string allows you to filter the sales only from the given date
        :param token: Next page token argument, leave at is it, only give 0 is you want the first page"""
        if token == -1:
            token = self.nexttoken
        url = self.url + "action=getcurrentsales&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version
        if prepurchase is not False:
            url += "&ispendingorder=y"
        if len(datefrom) != 0:
            url += "&purchasedate=" + str(datefrom)
        if token != 0 and self.nexttoken != 0:
            url += "&nexttoken=" + str(self.nexttoken)
        elif token != 0 and token > 0:
            url += "&nexttoken=" + str(token)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/getcurrentsales")
        self.nexttoken = self.__get_next_token(dictionary)
        return dictionary

    def get_billing_information(self, purchaseid):
        """Calling this method gives you accounting information about a confirmed order.
        :param purchaseid: is mandatory (same as found in get_new_sales report)."""
        purchaseid = str(purchaseid)
        url = self.url + "action=getbillinginformation&login=" + self.login\
            + "&pwd=" + self.pwd \
            + "&version=" + self.version\
            + "&purchaseid=" + str(purchaseid)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/getbillinginformation")
        return dictionary

    def get_shipping_information(self, purchaseid):
        """Quite similar to billing information method, but returns information about shipping for a given purchaseid
        Order forms are also available from this method return.
        :param purchaseid: is mandatory (same as found in get_new_sales report)."""
        purchaseid = str(purchaseid)
        url = self.url + "action=getshippinginformation&login=" + self.login\
            + "&pwd=" + self.pwd \
            + "&version=" + self.version\
            + "&purchaseid=" + str(purchaseid)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/getshippinginformation")
        return dictionary

    def get_items_todo_list(self):
        """Retriving a todo list on items, such as CLAIMS or MESSAGES from buyer or PriceMinister."""
        url = self.url + "action=getitemtodolist&login=" + self.login\
            + "&pwd=" + self.pwd \
            + "&version=" + self.version
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/getitemtodolist")
        return dictionary

    def get_items_info(self, itemid):
        """This methods retrieves informations from an "itemid" item, such as state, history, messages linked to it
        and actions available for this item. WARNING : All messages related to asked item will be tagged as "read"."""
        url = self.url + "action=getiteminfos&login=" + self.login\
            + "&pwd=" + self.pwd \
            + "&version=" + self.version \
            + "&itemid=" + str(itemid)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/getiteminfos")
        return dictionary

    def cancel_item(self, itemid, comment):
        """This method cancel the sale from the "itemid" item, after this one has been sold. WARNING : Cancelling
        a sale this way could harm your seller reputation. Use the "comment" param to specify the reason of this
        action to the related buyer (mandatory)."""
        url = self.url + "action=cancelitem" + "&itemid=" + str(itemid) \
            + "&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version \
            + "&comment=" + str(comment)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/cancelitem")
        return dictionary

    def contact_us_about_item(self, itemid, message, mailparentid):
        """This functionality permits to join the PriceMinister after-sales service as buyer or seller."""
        #TODO Contact WebServices support about mandatory mailparentid, what about a first contact with after-sales? (no ID available)
        pass

    def contact_user_about_item(self, itemid, message):
        """Contact buyer of the "itemid" item in a regular way, sending him the "message"""
        url = self.url + "action=contactuseraboutitem" + "&itemid=" + str(itemid) \
            + "&content=" + str(message) \
            + "&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/contactuseraboutitem")
        return dictionary

    def set_tracking_package_infos(self, itemid, transporter_name, tracking_number, tracking_url=""):
        """Send to buyer tracking infos, such as the transporter's name "transporter_name",
        tracking number "tracking_number" and the optional tracking url "trackin_url".
        Please note that giving "Autre" as transporter_name brings the tracking url as mandatory."""
        assert (transporter_name == "Autre" and len(tracking_url) == 0, "error : tracking url is mandatory")
        url = self.url + "action=settrackingpackageinfos" + "&itemid=" + str(itemid) \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version \
            + "&login=" + self.login \
            + "&transporter_name=" + str(transporter_name) \
            + "&tracking_number=" + str(tracking_number)
        if len(tracking_url) > 0:
            url += "&tracking_url=" + str(tracking_url)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/settrackingpackageinfos")
        return dictionary

    def confirm_preorder(self, advertid, stock):
        """Confirms preorders from the "advertid" item announce, will confirm "stock" items as confirmed orders."""
        assert (stock <= 0, "error : stock must be a positive number")
        url = self.url + "action=confirmpreorder" + "&login=" + self.login \
            + "&pwd=" + self.pwd \
            + "&version=" + self.version \
            + "&advertid=" + str(advertid) \
            + "&stock=" + str(stock)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/settrackingpackageinfos")
        return dictionary