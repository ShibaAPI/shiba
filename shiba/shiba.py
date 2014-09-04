__author__ = "boguta_m"

import urllib2 as ul
import xmltodict as x2d


class Shiba(object):
    def __init__(self, login, pwd, domain="https://ws.priceminister.com/"):
        """
        :param login: PriceMinister Seller login
        :param pwd: PriceMinister Seller Token
        (see more at https://developer.priceminister.com/blog/fr/documentation/identification-by-token)
        :param domain: give it the sanbox domain version of WebServices if you want to test this interface
        on a sandboxed version of PriceMinister
        """
        self.login = str(login)
        self.pwd = str(pwd)
        self.domain = domain

    @staticmethod
    def retrieve_dict_from_url(url):
        """Give it an , will send you back a full dictionary based on received XML from WebService.
        :rtype : dictionary"""
        xml = ul.urlopen(url).read()
        ret = x2d.parse(xml, process_namespaces=False)
        return ret

    @staticmethod
    def __create_xml_from_item_dict(inv):
        """Generate XML from the "inv" parameter, which is a dictionary hierarchized as the XML structure described
        in the WebServices documentation"""
        xml = x2d.unparse(inv)
        return xml