class ShibaTools(object):
    """Tools used by Shiba data retrieving classes"""
    @staticmethod
    def retrieve_dict_from_url(url):
        """Give it an , will send you back a full dictionary based on received XML from WebService.
        :rtype : dictionary"""
        xml = ul.urlopen(url).read()
        f = open("xmldump", "w")
        f.write(xml)
        ret = x2d.parse(xml, process_namespaces=False)
        return ret

    @staticmethod
    def __create_xml_from_item_dict(inv):
        """Generate XML from the "inv" parameter, which is a dictionary hierarchized as the XML structure described
        in the WebServices documentation"""
        xml = x2d.unparse(inv)
        return xml

    def dictanalysis(self):
        pass