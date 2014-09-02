import urllib2 as UL
import xmltodict as X2D


class ShibaMain(object):
    def __init__(self, login, pwd, version):
        """
        :param login: PriceMinister Seller login
        :param pwd: PriceMinister Seller Token (see more at https://developer.priceminister.com/blog/fr/documentation/identification-by-token)
        :param version: PriceMinister WebServices version (usually formated as yyyy-mm-dd)
        """
        self.login = str(login)
        self.pwd = str(pwd)
        self.version = str(version)

    def retrieve_dict_from_url(self, url, namespace):
        """#Give it an URL and a namespace to skip, will send you
        back a full dictionary based on received XML from WebService"""
        namespaces = {namespace: None}
        xml = UL.urlopen(url).read()
        ret = X2D.parse(xml, process_namespaces=True, namespaces=namespaces)
        return ret