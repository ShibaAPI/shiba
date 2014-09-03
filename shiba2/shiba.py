__author__ = "boguta_m"

import urllib2 as ul
import xmltodict as x2d


class Shiba(object):
    def __init__(self, login, pwd, version, mode=""):
        """
        :param login: PriceMinister Seller login
        :param pwd: PriceMinister Seller Token
        (see more at https://developer.priceminister.com/blog/fr/documentation/identification-by-token)
        :param version: PriceMinister WebServices version (usually formated as yyyy-mm-dd)
        :param mode: give it "test" if you want to test this interface on a sandboxed version of PriceMinister
        """
        self.login = str(login)
        self.pwd = str(pwd)
        self.version = str(version)
        if mode is "test":
            self.url = "https://ws.sandbox.priceminister.com/sales_ws?"
        else:
            self.url = "https://ws.priceminister.com/sales_ws?"

    @staticmethod
    def __retrieve_dict_from_url(url, namespace):
        """Give it an URL and a namespace to skip, will send you
        back a full dictionary based on received XML from WebService.
        :rtype : dictionary"""
        namespaces = {namespace: namespace}
        xml = ul.urlopen(url).read()
        ret = x2d.parse(xml, process_namespaces=True, namespaces=namespaces)
        return ret

    @staticmethod
    def __get_next_token(xml):
        """This method permits to get a nexttoken value for scrolling into multiple pages result, give it a parsed
        xml string into dictionary as parameter. If no token can be found, returns 0."""
        primarynode = xml.keys()[0]
        token = int(xml[primarynode]["response"]["nexttoken"])
        inttoken = int(token)
        return inttoken if inttoken > 0 else 0
