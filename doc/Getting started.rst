Getting started with Shiba
==========================

Installing
----------
You can get Shiba from PyPi python packet manager or directly from the GitHub repository:

- From **PyPi**:

  ``$ sudo pip install shiba``
 
- Download the .tgz from the GitHub repository, extract, and run:

  ``$ setup.py install``

- From Git:

  ``$ git clone git://github.com/shibaAPI/shiba.git && cd shiba && python setup.py install``

  If you have some errors while installing requirements, please install lxml from your package manager.

How does this works?
--------------------
First, import the main *Shiba* module, and create an instance of the *shibaconnection.ShibaConnection* class with your login, account token and domain if you want to work on the sanboxed version of the *PriceMinister WebServices*.

Then all you have to do is importing the management module you wish to work with, giving it your instanced connection class, and start dealing with those WebServices through its methods.

I want an example!
------------------
.. highlight:: python

This example will show you how to get new sales information on your seller account::

    from Shiba.shibaconnection import ShibaConnection
    from Shiba.salesmanagement import SalesManagement

    init = ShibaConnection("mysellerlogin", "mytokenpwd"[, sandbox=True """For testing purpose only (use Sandbox IDs)"""])
    salestool = SalesManagement(init)
    newsales = salestool.get_new_sales()

Now you can scroll the `ShibaResponseObject` object returned by the method::

    purchaseid = newsales.content.response.sales.sale[0].purchaseid # Getting the first sale on the list, retrieving the purchase ID
    purchasedate = newsales.content.response.sales.sale[0].purchasedate # Retrieving the purchase date
    for each in newsales.content.iterchildren():
        print each.tag # Will print each tag nodes from the first level
    print newsales.namespace # Will print the current namespace (not that useful, but can help for some cases of further development)
    print newsales.rawxml # Display the whole XML returned from WebServices and processed by Shiba

And here we go! All you have to do is to find the methods fitting your needs.

Testing
-------
Shiba comes with its tests, both offline and online ones.

*New in 1.1.2*: Tests now running with mock.

Offline testing
^^^^^^^^^^^^^^^
Move into the *offline* subdirectory of *tests/*, and simply run *nosetests*.

Online testing
^^^^^^^^^^^^^^
If you want to run online test, you will primary need to get a **PriceMinister sandbox account** in order to proceed.

Then open up the *tests/online/Assets/nosetests.cfg* file and fill it up with your sandbox **login** and **token** (not password).

Then simply run *nosetests* inside the *online* tests folder.
