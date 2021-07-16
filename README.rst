Shiba
=====

**Shiba** is a Python package that provides interfaces to **PriceMinister Web services**. Currently, all features works
with *Python3.x*. (3.6, 3.7, 3.8, 3.9)

Shiba supports all the Web services introduced by the *PriceMinister developper blog*.

The goal of Shiba is to provide PriceMinister active buyers/sellers an easy way to do their daily tasks for a good management
of their account.


Installation
------------

Install via `pip`_:

::

	$ pip install shiba

Install from source:

::

	$ git clone git://github.com/shibaAPI/shiba.git
	$ cd shiba
	$ python setup.py install


Quick starting with Shiba
-------------------------

Import the *shibaconnection* module first, then the module(s) you wish to work with.

Instance the *ShibaConnection* class with your credentials, then instance the other modules with the newly created *ShibaConnection* instance.

You're good to go!


*Example:*

::

	from shiba.shibaconnection import ShibaConnection
	from shiba.salesmanagement import SalesManagement

	connection = ShibaConnection("mylogin", "mytoken")
	sales = SalesManagement(connection)
	newsales = sales.get_new_sales()

Testing Shiba
-------------

**Shiba** comes with its bunch of tests.
Please refer to documentation for some information about testing options.


Documentation
-------------
Documentation is available on `GitHub pages`_.

Extra documentation from the `PriceMinister developper blog`_ might be useful.

Feel free to comment, report bugs, or even contribute!

*Thank you!*

.. _pip: http://pip-installer.org/
.. _GitHub pages: http://ShibaAPI.github.io/shiba/
.. _PriceMinister developper blog: https://developer.priceminister.com/blog/
