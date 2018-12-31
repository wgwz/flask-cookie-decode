flask-cookie-decode
###################

.. image:: https://travis-ci.org/wgwz/flask-cookie-decode.svg?branch=master
    :target: https://travis-ci.org/wgwz/flask-cookie-decode

.. contents::

.. section-numbering::

Purpose
=======

Adds a ``cookie`` command to the built-in Flask CLI which will provide various
tools for debugging the secure session cookie that Flask uses by default.

Current available commands:

* `flask cookie decode`: decodes and verifies the signature of the session cookie

Background
==========

By default the Flask session uses a signed cookie to store its data. The Flask
application signs the cookie using its ``SECRET_KEY``. This provides the Flask
application a way to detect any tampering to the session data. If the application
is indeed using a secret key and secure hashing algorithm, the session signature
will be unique to application. 

At times during development or when a user encounters an error, you might want to
inspect the session cookie. This extension looks to provide an easy-to-use interface
for inspecting session cookies for development and debugging purposes.

For more on the topic of the Flask session see these references:

* `How Secure Is The Flask User Session?`_
* `Quickstart for Flask Sessions`_
* `API Docs for Flask Sessions`_

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

Using the CLI
-------------

Example ``app.py``:

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

Using the CLI:

.. code-block:: bash

    $ export FLASK_APP=app.py
    $ flask cookie decode eyJhIjoiYXNkYXNkamtqYXNkIn0.XCkk1Q.tTPu2Zhvn9KxgkP35ERAgyd8MzA
    {'a': 'asdasdjkjasd'}

Include expiration timestamp:

.. code-block:: bash

    $ flask cookie decode --timestamp eyJhIjoiYXNkYXNkamtqYXNkIn0.XCkk1Q.tTPu2Zhvn9KxgkP35ERAgyd8MzA
    ({'a': 'asdasdjkjasd'}, datetime.datetime(2018, 12, 30, 20, 4, 37))

Documentation
=============

* `readthedocs <https://flask-cookie-decode.readthedocs.io/en/latest/>`_

License
=======

MIT: `LICENSE <https://github.com/wgwz/flask-cookie-decode/blob/master/LICENSE>`_.

.. _`How Secure Is The Flask User Session?`: https://blog.miguelgrinberg.com/post/how-secure-is-the-flask-user-session
.. _`Quickstart for Flask Sessions`: http://flask.pocoo.org/docs/1.0/quickstart/#sessions
.. _`API Docs for Flask Sessions`: http://flask.pocoo.org/docs/1.0/api/#sessions
