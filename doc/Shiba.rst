Shiba, from A to Z
==================

About Shiba sub management modules
----------------------------------
All submodules included from the main **Shiba** package needs an instanced *ShibaConnection* class
defining your login and an identification token as parameter.

You can also tell it to deal with the sanboxed
version for testing purposes.

**Each method of each submodule** returns a *ShibaResponseObject* element from the
XML returned by the PriceMinister WebServices, give it a look from the section dedicated for this class.

ShibaResponseObject wraps an *ObjectifiedElement* from the *lxml.objectify* module as the main container for the retrieved data. This object is callabel through the *content* attribute.

You can find some documentation about it looking into the lxml documentation_.

.. _documentation: http://lxml.de/objectify.html

AccountingManagement module
---------------------------

.. automodule:: shiba.accountingmanagement
    :members:
    :undoc-members:
    :show-inheritance:

InventoryManagement module
--------------------------

.. automodule:: shiba.inventorymanagement
    :members:
    :undoc-members:
    :show-inheritance:

MarketplaceManagement module
----------------------------

.. automodule:: shiba.marketplacemanagement
    :members:
    :undoc-members:
    :show-inheritance:

SalesManagement module
----------------------

.. automodule:: shiba.salesmanagement
    :members:
    :undoc-members:
    :show-inheritance:

ShibaResponseObject module
--------------------------
Containing the object class returned by each method of the modules above.

.. automodule:: shiba.shibaresponseobject
    :members:
    :undoc-members:
    :show-inheritance:

Shiba login ShibaConnection class
---------------------------------

.. automodule:: Shiba.shibaconnection
    :members:
    :undoc-members:
    :show-inheritance:

Shiba exception classes
-----------------------

.. automodule:: shiba.shibaexceptions
    :members:
    :undoc-members:
    :show-inheritance:
