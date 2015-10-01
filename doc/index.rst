.. Shiba documentation master file, created by
   sphinx-quickstart on Thu Sep 11 13:24:19 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===================================================
Shiba - An Python API for PriceMinister WebServices
===================================================


Welcome to Shiba's documentation!
=================================
This is the documentation for the `Shiba API`_ project on GitHub.

Hope you will find what you're looking for!

What is Shiba?
--------------
**Shiba** is an API intended to bring an human handlable utilisation of the **PriceMinister WebServices** with **Python**.

It works through modules, imported to your scripts to fit your needs.

Contents
________

.. toctree::
   :maxdepth: 2

   Getting started
   Shiba

Releases and changelog
----------------------
**8-Dec-2014** *1.1.2* : Set up a new explicit exception for throttling from PriceMinister, named *ShibaQuotaExceededError*. Testing is now available both offline (using mock XML) and online.

**24-Sep-2014** *1.1.1* : Added explicit and mandatory required dependencies to *setup.py*, indeed installing Shiba before didn't install those.

Changed package name from *Shiba* to *shiba*, according to the naming conventions.

**22-Sep-2014** *1.1* : Return content from the Shiba methods is now more polyvalent, as its own object call *ShibaResponseObject*. The *content* attribute from returns is the previous *obj* itself, namespace freed. Namespace can be found into the *namespace* attribute, and raw XML from the Web Services is also now available into the *rawxml* attribute of the *ShibaResponseObject* class.

**12-Sep-2014** *1.0.1* : Fixed bug on listing using lists as refs or product IDs.

**11-Sep-2014** *1.0* : Initial release.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Shiba API: https://github.com/ShibaAPI/shiba
