Pythonic Interface to BentoSign
===============================

This Python package offers a Pythonic interface to the BentoSign API.
It is used by developers to manage Bento data.

Installation
------------

::

    pip install bentosign

Typical usage
-------------

::

    import bentosign

    # Retrieve a list of packages using a name filter
    packages = bentosign.Package.find(name='%One%')

    # Create a new signing Process for a specific Recipient and Package
    process = bentosign.Process.create(email='ling.thio@gmail.com', package_name='Package One')
