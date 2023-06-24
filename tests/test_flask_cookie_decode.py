#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

"""
test_flask_cookie_decode
----------------------------------

Tests for `flask_cookie_decode` module.
"""
import datetime
import json
from click.testing import CliRunner
import pytest
from flask_cookie_decode.__main__ import decode
from flask_cookie_decode import CookieDecode
from flask_cookie_decode.cookie_decode import (
    TrustedCookie,
    ExpiredCookie,
    UntrustedCookie,
)
import itsdangerous

foo_app_secret = "jlghasdghasdhgahsdg"
foo_cookie = "eyJhIjoiaGVsbG93b3JsZCJ9.XCfs8A.v910WSXgY5JhZJHZ_nCNCYsy2I0"
foo_cookie_invalid_sign = "eyJhIjoiaGVsbG93b3JsZCJ9.XCfs8A.10WSXgY5JhZJHZ_nCNCYsy2I0"
foo_compressed_cookie = ".eJxNkM1KBEEMhF-lmPMwD-BNUEFQj96zPXE20D-z-VkE8d3N7oJ6aZruVH2V-ppouptehnKD7BYN66hDYeKgxj6jjG5cnD0UtMouVqRv4Cq-4L7KKajhzOZyiJr6RmYE3thReeRP504uBunOukZb8P43HY5Dpb4m7iqccwz7UCd0PgUnIg2o4yxnViV8UJEqln5drM430NBOysnKUHkepUSl9F7wMDoXkJbI-cNxRk19FwKVBH5Ki0uwGTvXyhnQkok-OliHLXil0H_RkSVkARcQNFyv61a2oJUWPIUVBsEzflbIgdSm_55MVnI4tz3S9Y2ui59JJb8bbT3Vjy7XIiv20Hy-FfycSbJI2S4L5S2b-60iVzcnW6bvH4O_pXE.XCfoTg.D-eoYNfJpJiyAyBFiUQ4JLUGevQ"
foo_cookie_expired = ".eJyrVkpUslJKzMpISUvMAKIUIJGTnZKWkQjCWcVgVhaQyM4CC2SDFWSBVCjVAgC93hdR.XDFEIg.Sw2azr8qJi8UDWUKyC7fKTDUIcs"
rv_foo_cookie = ({"a": "helloworld"}, "2019-01-29T21:53:52")
rv_foo_cookie_invalid_sign = ({"a": "helloworld"}, "2019-01-29T21:53:52")
rv_foo_cookie_expired = (
    {"a": "ajhdfahfahdhfalkdfhadfhajsdfhadjfhakjdfhajkdhfaljkdfh"},
    "2019-02-05T23:56:18",
)


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config.update({"SECRET_KEY": foo_app_secret})
    cookie = CookieDecode()
    cookie.init_app(app)
    return app


@pytest.fixture
def fcd_invoke():
    runner = CliRunner()

    def _invoke(cookie):
        return runner.invoke(decode, [cookie])

    return _invoke


def test_fcd(fcd_invoke):
    res = fcd_invoke(foo_cookie)
    assert res.exit_code == 0
    assert "a" in json.loads(res.output).keys()


def test_fcd_compress(fcd_invoke):
    res = fcd_invoke(foo_compressed_cookie)
    assert res.exit_code == 0
    assert "a" in json.loads(res.output).keys()


def test_safe_decode(app):
    result = app.extensions["flask_cookie_decode"]._safe_decode(foo_cookie)
    assert result[0] == rv_foo_cookie[0]
    assert result[1].replace("+00:00", "") == rv_foo_cookie[1]


def test_unsafe_decode(app):
    result = app.extensions["flask_cookie_decode"]._unsafe_decode(foo_cookie)
    assert result == ({"a": "helloworld"}, None)


def test_safe_decode_invalid_sign(app):
    with pytest.raises(itsdangerous.exc.BadTimeSignature) as excinfo:
        app.extensions["flask_cookie_decode"]._safe_decode(foo_cookie_invalid_sign)


def test_unsafe_decode_invalid_sign(app):
    result = app.extensions["flask_cookie_decode"]._unsafe_decode(
        foo_cookie_invalid_sign
    )
    assert result == ({"a": "helloworld"}, None)


def test_compressed_safe_decode(app):
    result = app.extensions["flask_cookie_decode"]._safe_decode(foo_compressed_cookie)
    assert result[0] == {
        "a": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam vestibulum massa eget leo venenatis interdum. Vestibulum ut blandit massa, in porta neque. Aenean viverra facilisis nisl, eget ornare velit vehicula ut. Donec arcu nibh, lacinia ac maximus in, pellentesque non eros. Mauris interdum turpis vel rutrum malesuada. Fusce a tortor eu risus placerat tempus. Nam ut varius magna. Etiam vel purus elit. In et ligula et est viverra egestas."
    }
    assert result[1].replace("+00:00", "") == "2019-01-29T21:34:06"


def test_decode_cookie_trusted(app):
    result = app.extensions["flask_cookie_decode"].decode_cookie(foo_cookie)
    expect = TrustedCookie(*rv_foo_cookie)
    assert result.contents == expect.contents
    assert result.expiration.replace("+00:00", "") == expect.expiration


def test_decode_cookie_untrusted(app):
    result = app.extensions["flask_cookie_decode"].decode_cookie(
        foo_cookie_invalid_sign
    )
    expect = UntrustedCookie(*rv_foo_cookie_invalid_sign)
    assert result.contents == expect.contents
    assert result.expiration.replace("+00:00", "") == expect.expiration


def test_decode_cookie_expired(app):
    result = app.extensions["flask_cookie_decode"].decode_cookie(foo_cookie_expired)
    expect = ExpiredCookie(*rv_foo_cookie_expired)
    assert result.contents == expect.contents
    assert result.expiration.replace("+00:00", "") == expect.expiration
