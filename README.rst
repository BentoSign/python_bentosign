Pythonic Interface to Bento
===========================

This Python package offers a Pythonic interface to the Bento RESTful API.
It is used by developers to manage Bento data.

Installation
------------

::
    pip install bento
    pip install bentosign

Typical usage
-------------

::
    import bento
    import bentosign

    auth_token = bento.authenticate()
    package = bentosign.Package.get(name='Some package name')
    recipient = bentosign.Recipient.get(email='recipient@example.com')
    process = bentosign.Process.create(package_id=package.id, recipient_id=recipient.id)
