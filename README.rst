flask-cookie-decode
###################

.. list-table::

    * - .. image:: https://github.com/wgwz/flask-cookie-decode/actions/workflows/action.yml/badge.svg
          :target: https://github.com/wgwz/flask-cookie-decode/actions
          :alt: Github Build Status
    
    * - .. image:: https://readthedocs.org/projects/flask-cookie-decode/badge/?version=latest
          :target: https://flask-cookie-decode.readthedocs.io/en/latest/?badge=latest
          :alt: Documentation Status

.. contents::

.. section-numbering::

Purpose
=======

Adds a ``cookie`` command to the built-in Flask CLI which will provide various
tools for debugging the secure session cookie that Flask uses by default.

Current available commands
--------------------------

1. `flask cookie decode`: decodes and verifies the signature of the session cookie

Background
==========

By default the Flask session uses a signed cookie to store its data. The Flask
application signs the cookie using its ``SECRET_KEY``. This provides the Flask
application a way to detect any tampering to the session data. If the application
is indeed using a secret key and secure hashing algorithm, the session signature
will be unique to application.

For more on the topic of the Flask session see these references:

* `How Secure Is The Flask User Session?`_
* `Quickstart for Flask Sessions`_
* `API Docs for Flask Sessions`_

.. _`How Secure Is The Flask User Session?`: https://blog.miguelgrinberg.com/post/how-secure-is-the-flask-user-session
.. _`Quickstart for Flask Sessions`: http://flask.pocoo.org/docs/1.0/quickstart/#sessions
.. _`API Docs for Flask Sessions`: http://flask.pocoo.org/docs/1.0/api/#sessions
.. _`Flask Session Cookie Decoder`: https://www.kirsle.net/wizards/flask-session.cgi

Disclaimer: Keep your SECRET_KEY, secret!
-----------------------------------------

If you expose this key your application becomes vulnerable to session replay
attacks. `Here is an example`_ where an application exposed the ``SECRET_KEY``
during 404 errors. The example also illustrates how session replay works.

By default Flask does not expose the ``SECRET_KEY`` anywhere. It is up to you
the developer to keep it that way!

.. _`Here is an example`: https://terryvogelsang.tech/MITRECTF2018-my-flask-app/

Usage
=====

Installation
------------

.. code-block:: bash

    $ pip install flask-cookie-decode

Extracting the cookie using browser tools
-----------------------------------------

.. image:: https://raw.githubusercontent.com/wgwz/flask-cookie-decode/master/docs/cookie.png
    :alt: Finding the cookie in browser tools
    :width: 100%
    :align: center

Example Flask app
-----------------

See `examples/app.py <https://github.com/wgwz/flask-cookie-decode/blob/master/examples/app.py>`_:

.. code-block:: python

    from flask import Flask, jsonify, session, request
    from flask_cookie_decode import CookieDecode

    app = Flask(__name__)
    app.config.update({'SECRET_KEY': 'jlghasdghasdhgahsdg'})
    cookie = CookieDecode()
    cookie.init_app(app)

    @app.route('/')
    def index():
        a = request.args.get('a')
        session['a'] = a
        return jsonify(dict(session))

Examples using the CLI:
-----------------------

This extension will ship two CLI interfaces for dealing with decoding cookies. One requires a Flask application instance for the application you are wanting to debug. This method has the added benefit that the signature of the cookie can be verified, as your application instance has the ``SECRET_KEY`` used to sign the cookie. This method returns decoded cookie objects which can be seen in the examples below. This method can return a few different types of cookie objects depending on the state of the cookie. Please keep in mind that this extension provides only a thin-wrapper around the logic Flask uses to deal with cookies.

The second CLI interface is a tool for decoding cookies without the app secret. It cannot validate the signatures on the cookies or check the expirations and does not require the application instance like the other CLI. Intended for debugging purposes only.

CLI attached to application instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. A cookie with a valid signature:

.. code-block:: bash

    $ export FLASK_APP=app.py
    $ flask cookie decode eyJhIjoiYXNkYXNkamtqYXNkIn0.XCkk1Q.tTPu2Zhvn9KxgkP35ERAgyd8MzA
    TrustedCookie(contents={'a': 'asdasdjkjasd'}, expiration='2019-01-30T20:04:37')

2. A cookie with an invalid signature:

.. code-block:: bash

    $ export FLASK_APP=app.py
    $ flask cookie decode eyJhIjoiYXNkYXNkamtqYXNkIn0.XCkk1Q.tTPu2Zhvn9KxgkP35ERAgyd8MzA
    UntrustedCookie(contents={'a': 'asdasdjkjasd'}, expiration='2019-01-30T20:04:37')

3. An expired cookie:

.. code-block:: bash

    $ export FLASK_APP=app.py
    $ flask cookie decode eyJhIjoiYXNkYXNkamtqYXNkIn0.XCkk1Q.tTPu2Zhvn9KxgkP35ERAgyd8MzA
    ExpiredCookie(contents={'a': 'asdasdjkjasd'}, expiration='2019-01-30T20:04:37')

CLI that ships with package which only decodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ fcd decode eyJhIjoiYXNkYXNkamtqYXNkIn0
    {
      "a": "asdasdjkjasd"
    }

Documentation
=============

`Docs <https://flask-cookie-decode.readthedocs.io/en/latest/>`_

License
=======

`MIT <https://github.com/wgwz/flask-cookie-decode/blob/master/LICENSE>`_.
