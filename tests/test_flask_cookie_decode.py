#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

"""
test_flask_cookie_decode
----------------------------------

Tests for `flask_cookie_decode` module.
"""
import datetime
import pytest
from flask_cookie_decode import CookieDecode

foo_app_secret = 'jlghasdghasdhgahsdg' 

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config.update({'SECRET_KEY': foo_app_secret})
    cookie = CookieDecode()
    cookie.init_app(app)
    return app

foo_cookie = 'eyJhIjoiaGVsbG93b3JsZCJ9.XCfs8A.v910WSXgY5JhZJHZ_nCNCYsy2I0'
foo_compressed_cookie = '.eJxNkM1KBEEMhF-lmPMwD-BNUEFQj96zPXE20D-z-VkE8d3N7oJ6aZruVH2V-ppouptehnKD7BYN66hDYeKgxj6jjG5cnD0UtMouVqRv4Cq-4L7KKajhzOZyiJr6RmYE3thReeRP504uBunOukZb8P43HY5Dpb4m7iqccwz7UCd0PgUnIg2o4yxnViV8UJEqln5drM430NBOysnKUHkepUSl9F7wMDoXkJbI-cNxRk19FwKVBH5Ki0uwGTvXyhnQkok-OliHLXil0H_RkSVkARcQNFyv61a2oJUWPIUVBsEzflbIgdSm_55MVnI4tz3S9Y2ui59JJb8bbT3Vjy7XIiv20Hy-FfycSbJI2S4L5S2b-60iVzcnW6bvH4O_pXE.XCfoTg.D-eoYNfJpJiyAyBFiUQ4JLUGevQ'

def test_decode(app):
    assert app.extensions['flask_cookie_decode'].decode(foo_cookie) == {'a': 'helloworld'}

def test_decode_with_timestamp(app):
    assert app.extensions['flask_cookie_decode'].decode(foo_cookie, return_timestamp=True) == ({'a': 'helloworld'}, datetime.datetime(2018, 12, 29, 21, 53, 52))

def test_compressed_decode(app):
    assert app.extensions['flask_cookie_decode'].decode(foo_compressed_cookie) == {
        'a': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam vestibulum massa eget leo venenatis interdum. Vestibulum ut blandit massa, in porta neque. Aenean viverra facilisis nisl, eget ornare velit vehicula ut. Donec arcu nibh, lacinia ac maximus in, pellentesque non eros. Mauris interdum turpis vel rutrum malesuada. Fusce a tortor eu risus placerat tempus. Nam ut varius magna. Etiam vel purus elit. In et ligula et est viverra egestas.'
    }
