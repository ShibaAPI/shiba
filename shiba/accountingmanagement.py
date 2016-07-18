# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from shibaconnection import ShibaConnection
from shibaexceptions import ShibaCallingError
from shibatools import inf_constructor, url_constructor, retrieve_obj_from_url


class AccountingManagement(object):
    """Accounting Management class, showing global financial operations on your account, or specific financial details
        about an operation"""
    def __init__(self, connection):
        assert(isinstance(connection, ShibaConnection)),\
            "error : you must give this instance a ShibaConnection instance"
        self.connection = connection

    def get_operations(self, lastoperationdate=""):
        """Get global operations which happened on your wallet, compensationid given back from XML can be used
        in the get_compensation_details method below to get more detailed information about a specific operation.

        :param lastoperationdate: as follows : dd/mm/yyyy-hh:mm:ss and as string or date instance.
        """
        operationcause = "salestransfer"
        if isinstance(lastoperationdate, date) is False and type(lastoperationdate) is not str and \
                type(lastoperationdate) is not unicode:
            raise ShibaCallingError("Shiba code error : lastoperationdate parameter must be a datetime instance or str,"
                                    " got " + unicode(type(lastoperationdate)) + " instead.")
        if isinstance(lastoperationdate, date):
            lastoperationdate = lastoperationdate.strftime("%d/%m/%y-%H:%M:%S")
        inf = inf_constructor(self.connection, "getoperations", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj

    def get_compensation_details(self, compensationid):
        """Get a specific operation details from its "compensationid" found in the get_operation request return."""
        inf = inf_constructor(self.connection, "getcompensationdetails", **locals())
        url = url_constructor(self.connection, inf)
        obj = retrieve_obj_from_url(url)
        return obj
