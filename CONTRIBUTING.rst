.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/wgwz/flask-cookie-decode/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

flask-cookie-decode could always use more documentation, whether as part of the
official flask-cookie-decode docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/wgwz/flask-cookie-decode/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `flask_cookie_decode` for local development.

1. Fork the `flask_cookie_decode` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/flask-cookie-decode.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv flask_cookie_decode
    $ python3 -m virtualenv venv  # alternative way to create the virtualenv
    $ python3 -m venv venv  # alternative way to create the virtualenv
    $ . venv/bin/activate  # if not using virtualenvwrapper
    $ cd flask-cookie-decode/
    $ pip install -e .

   If you wish to install some helpful tools for development use the ``dev-requirements.txt``::

    $ pip install -r dev-requirements.txt

   For example if you want to have the tests run automatically each time a file changes you can make use of ``pytest-watch``::

   $ cd flask-cookie-decode
   $ ptw

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox::

    $ flake8 flask_cookie_decode tests
    $ python setup.py test
    $ pytest  # alternative way to run the tests
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.7, 3.4, 3.5, and 3.6. Check
   https://travis-ci.org/wgwz/flask-cookie-decode/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ pytest tests::test_flask_cookie_decode

Making a release
----------------

Using towncrier for release notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
https://pypi.org/project/towncrier/

Automated build process
~~~~~~~~~~~~~~~~~~~~~~~

Notes on the initial set up travis-ci.com::

    $ travis logout
    $ travis login --pro
    $ travis encrypt --add deploy.password <pypi-password> --com  # within the flask-cookie-decode repo

See travis.rb_, dpl_ and `travis encryption keys`_ for more on the travis set up.

.. _travis.rb: https://github.com/travis-ci/travis.rb#installation
.. _dpl: https://github.com/travis-ci/dpl#pypi
.. _travis encryption keys: https://docs.travis-ci.com/user/encryption-keys/

1. Bump the version and create the tag::

    $ git checkout master
    $ bumpversion <major,minor,patch>
    $ git tag -s v<latest-version> -m "tag message"

2. Push the tag, travis-ci will handle deployment to pypi. (see ``.travis.yml``)::

    $ git push origin v<latest-version>

Manual build process
~~~~~~~~~~~~~~~~~~~~

Notes on manual upload of releases to pypi:

1. Run the release commands::

    $ git checkout v<latest-version>
    $ make dist
    $ twine upload dist/*

2. Go to github releases and upload wheel and tar.gz
