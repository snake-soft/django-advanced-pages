.. image:: https://api.codeclimate.com/v1/badges/cfd2071c8e13d1eab244/maintainability
   :target: https://codeclimate.com/github/snake-soft/django-advanced-pages/maintainability
   :alt: Maintainability

.. image:: https://codecov.io/gh/snake-soft/django-advanced-pages/branch/main/graph/badge.svg?token=X9MJQJBAEH
   :target: https://codecov.io/gh/snake-soft/django-advanced-pages
    
=====================
Django advanced pages
=====================

With this you can enhance the Django flatpages app by some features.


Features
--------

* Categorize pages
* Original Django flatpages are not touched
* Priorize the pages
* Categorize the pages
* Admin loads the enhanced model instead of the flatpages


Installation
------------

Install using pip:

.. code-block:: bash

	pip install django-advanced-pages


You need to load both, advanced and original pages because this package uses onetoone field to enhance the original Django Flatpages app:

.. code-block:: python

   # settings.py
   INSTALLED_APPS = [
       # ...
       'django.contrib.flatpages',
       'pages.apps.PagesConfig',
       # ...
   ]


You can pass the pages to the template like this:

.. code-block:: python

   from pages.models import Page, Category
   'pages': {
      'company': Page.objects.filter(category=Category.COMPANY),
      'legal': Page.objects.filter(category=Category.LEGAL),
   },
