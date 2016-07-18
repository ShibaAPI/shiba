# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class ShibaResponseObject(object):
    """This class gathers all content from the returned XML. Separating the namespace for further usage and the actual
    content. The raw XML from the WebServices is also reachable from this object.

    :param namespace: The namespace of the treated object, non really useful in our case but kept for further \
        development steps
    :param obj: The actual content of the returned XML, as an ObjectifiedElement from the lxml.objectify module
    :param xml: The raw XML returned by the WebServices

    Those arguments are stored into *content* for the ObjectifiedElement, *raw* for the raw and XML and *namespace* for
    the namespace of the XML, which have been removed.
    """

    def __init__(self, namespace, obj, xml):
        self.namespace = namespace
        self.content = obj
        self.rawxml = xml
