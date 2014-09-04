#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class InventoryManagementTest
# Testing runtime methods


import collections


class TestRuntime(object):
    """Class for some methods permittings to push some tests further"""
    def __init__(self):
        self.tmpcount = 0

    def __rec_dict_crawling(self, dictionary, tofind):
        for key in dictionary:
            cur = dictionary.get(key)
            print type(cur)
            if type(cur) is collections.OrderedDict:
                self.tmpcount += self.__rec_dict_crawling(cur, tofind)
            elif key == tofind:
                self.tmpcount += len(key)
        return self.tmpcount

    @staticmethod
    def fun(d):
        if 'id' in d:
          yield d['id']
        for k in d:
         if isinstance(d[k], list):
            for i in d[k]:
                for j in fun(i):
                    yield j

    def dictanalysis(self, dictionary, tofind="", nb=0):
        """Dictionary analysis, will crawl trough a dictionnary given by the "dict" parameter, searching for the
        "tofind" keys (can be a list),
        the "nb" parameter tells this methods how many occurences it has to find in the dictionary, its
        associated to the "tofind" list index. If the occurence amount is greater or fewer than "nb", this method will
        return False."""
        assert((type(nb) is list) or (type(nb) is int)), "error : bad 'nb' type given"
        assert((type(tofind) is list) or (type(tofind) is str)), "error : bad 'tofind' type given"
        nblist = [nb] if type(nb) is int else nb
        tflist = [tofind] if type(tofind) is str else tofind
        ocfound = []
        for index in range(0, len(tflist)):
            self.tmpcount = 0
            ocfound.append(self.__rec_dict_crawling(dictionary, tflist[index]))
        print(ocfound, nblist, nb, tofind)
        return False
        return True if (ocfound == nblist and nb != 0) or (nb == 0 and ocfound[0] > 0) else False