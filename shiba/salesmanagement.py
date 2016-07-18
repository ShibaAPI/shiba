# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from .shibaconnection import ShibaConnection
from .shibaexceptions import ShibaCallingError
from .shibatools import inf_constructor, url_constructor, retrieve_obj_from_url
from .compat import basestring


class SalesManagement(object):
    """Primary sales management class, gather all sales-related methods."""
    def __init__(self, connection):
        if (isinstance(connection, ShibaConnection)) is False:
            raise ShibaCallingError("error : you must give this class a ShibaConnection instance")
        self.connection = connection

    def get_new_sales(self):
        """Calling get_new_sales all the new sales which have been recently recensed."""
        inf = inf_constructor(self.connection, "getnewsales", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def accept_sale(self, itemid):
        """Accept the "itemid" sale.

        :param itemid: string for item ID
        """
        inf = inf_constructor(self.connection, "acceptsale", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def refuse_sale(self, itemid):
        """Refuse the "itemid" sale.

        :param itemid: string for item ID
        """
        inf = inf_constructor(self.connection, "refusesale", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def get_current_sales(self, ispendingpreorder="", purchasedate="", nexttoken=""):
        """Calling get_current_sales method gives you a obj gathering all current sales.

        :param ispendingpreorder: pass "y" is you want to see all preordered sales, leave empty as default
        :param purchasedate: Formatted as "yyyy-mm-dd" string allows you to filter the sales only from the given date
        :param nexttoken: Next page token argument, leave at is it, only give 0 is you want the first page
        """
        if ispendingpreorder != "" and ispendingpreorder != "y":
            raise ShibaCallingError("ispendingpreorder parameter must be empty or 'y'")

        if not isinstance(purchasedate, date) and not isinstance(purchasedate, basestring):
            raise ValueError("expected string or date for 'purchasedate', got '%s'" % type(purchasedate))

        if isinstance(purchasedate, date):
            purchasedate = purchasedate.strftime("%d/%m/%y-%H:%M:%S")
        inf = inf_constructor(self.connection, "getcurrentsales", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def get_billing_information(self, purchaseid):
        """Calling this method gives you accounting information about a confirmed order.

        :param purchaseid: is mandatory (same as found in get_new_sales report).
        """
        inf = inf_constructor(self.connection, "getbillinginformation", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def get_shipping_information(self, purchaseid):
        """Quite similar to billing information method, but returns information about shipping for a given purchaseid
        Order forms are also available from this method return content.

        :param purchaseid: is mandatory (same as found in get_new_sales report).
        """
        inf = inf_constructor(self.connection, "getshippinginformation", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def get_item_todo_list(self):
        """Retrieving a todo list on items, such as CLAIMS or MESSAGES from buyer or PriceMinister."""
        inf = inf_constructor(self.connection, "getitemtodolist", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def get_item_infos(self, itemid):
        """This methods retrieves information from an "itemid" item, such as state, history, messages linked to it
        and actions available for this item. WARNING : All messages related to asked item will be tagged as "read".

        :param itemid: string for item ID
        """
        inf = inf_constructor(self.connection, "getiteminfos", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def cancel_item(self, itemid, comment):
        """This method cancel the sale from the "itemid" item, after this one has been sold. WARNING : Cancelling
        a sale this way could harm your seller reputation. Use the "comment" param to specify the reason of this
        action to the related buyer (mandatory).

        :param itemid: string for item ID
        :param comment: message to send to the buyer as reason for cancelling the sale
        """
        inf = inf_constructor(self.connection, "cancelitem", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def contact_us_about_item(self, itemid, content, mailparentid):
        """This functionality permits to join the PriceMinister after-sales service as buyer or seller.
        Specify the mailparentid to reply to a previous mail exchange. Message is message content, and itemid is
        the item PriceMinister ID related to the claim.

        :param itemid: string for item ID
        :param content: message content
        :param mailparentid: ID of previous mail, you must have conversed with the customer before to get it
        """
        inf = inf_constructor(self.connection, "contactusaboutitem", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def contact_user_about_item(self, itemid, content):
        """Contact buyer of the "itemid" item in a regular way, sending him a message.

        :param itemid: string for item ID
        :param content: message content
        """
        inf = inf_constructor(self.connection, "contactuseraboutitem", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def set_tracking_package_infos(self, itemid, transporter_name, tracking_number, tracking_url=""):
        """Send to buyer tracking information, such as the transporter's name "transporter_name",
        tracking number "tracking_number" and the optional tracking url "tracking_url".
        Please note that giving "Autre" as transporter_name brings the tracking url as mandatory.
        This WebService send an email to the "itemid" customer, including a link for package tracking.

        :param itemid: string for item ID
        :param transporter_name: transporter's name, string expected
        :param tracking_number: tracking number, preferably as string
        :param tracking_url: tracking URL for the package, as string, mandatory if transporter_name is 'Autre'
        """
        if transporter_name == "Autre" and len(tracking_url) == 0:
            raise ShibaCallingError("Shiba code error : if 'Autre' is specified as transporter_name, a tracking_url "
                                    "must be specified too")
        inf = inf_constructor(self.connection, "settrackingpackageinfos", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def confirm_preorder(self, advertid, stock):
        """Confirms preorders from the "advertid" item announce, will confirm "stock" items as confirmed orders for
        buyers who has preordered from the advert.

        :param advertid: advert ID as string
        :param stock: string or integer, must be positive
        """
        if int(stock) <= 0:
            raise ShibaCallingError("Shiba code error : stock must be a positive number")
        inf = inf_constructor(self.connection, "confirmpreorder", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj
