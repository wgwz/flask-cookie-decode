History
#######

.. towncrier release notes start

Flask_Cookie_Decode 0.4.1 (2024-03-17)
======================================

Chores
------

- Added a github action that runs a test suite with variety of Python and Flask versions.
  The github action also builds and deploys the package to Pypi. (actions)


Flask_Cookie_Decode 0.4.0 (2023-06-23)
======================================

Bugfixes
--------

- remove dependency on flask.helpers.total_seconds (#13)


Flask_Cookie_Decode 0.3.2 (2019-11-29)
======================================

Bugfixes
--------

- The `fcd` client now handles compressed cookies. (#10)


Flask_Cookie_Decode 0.3.1 (2019-11-29)
======================================

Features
--------

- Add the `fcd` CLI for reading cookies without a flask app. (#8)


Flask_Cookie_Decode 0.3.0 (2019-01-05)
======================================

Bugfixes
--------

- In all previous releases the CLI with the ``--timestamp`` CLI flag was actually
  returning the timestamp when the cookie was signed. *Not* the timestamp when the
  cookie expires, as it should have been doing.

  In all previous releases there was no error handling for expired cookies. This
  release now returns a ``ExpiredCookie`` when it is detected. (#1)


Improved Documentation
----------------------

- Updates the documentation to include some more details about the way the
  Flask session works, and things you should be looking out for from a security
  perspective. The documentation also reflects the latest in terms of the way
  the CLI works. (#1)


0.1.0 (2018-12-29)
==================

* First release on PyPI.
