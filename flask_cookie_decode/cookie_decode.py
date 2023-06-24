from datetime import datetime, timedelta
from collections import namedtuple
import click
from itsdangerous.timed import TimestampSigner
from itsdangerous.exc import BadTimeSignature, SignatureExpired
from flask.cli import AppGroup
from flask.sessions import SecureCookieSessionInterface

TrustedCookie = namedtuple("TrustedCookie", "contents, expiration")
UntrustedCookie = namedtuple("UntrustedCookie", "contents, expiration")
ExpiredCookie = namedtuple("ExpiredCookie", "contents, expiration")


class CookieDecode(object):
    """This class is used to inspect the signed-cookie session that Flask
    ships with.  Initializing this class follows the usual procedure::

        app = Flask(__name__)
        cookie = CookieDecode(app)

    Or if you wish to create the object once and configure the application
    later to support it::

        cookie = CookieDecode()

        def create_app():
            app = Flask(__name__)
            cookie.init_app(app)
            return app

    Once the application has been initialized with the extension, a new command
    will be available via the Flask CLI::

        flask cookie decode <cookie-here>

    This command takes one argument, the Flask session cookie. The session cookie
    can be retrieved from a browser.

    Reference: https://blog.miguelgrinberg.com/post/how-secure-is-the-flask-user-session
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initalizes the application with the extension."""
        self._session_interface = SecureCookieSessionInterface()
        self._signing_serializer = self._session_interface.get_signing_serializer(app)
        self._timestamp_signer = TimestampSigner(
            app.secret_key, key_derivation="hmac", salt="cookie-session"
        )
        if isinstance(app.permanent_session_lifetime, timedelta):
            self._max_age = app.permanent_session_lifetime.total_seconds()
        else:
            self.max_age = app.permanent_session_lifetime

        cookie_cli = AppGroup(
            "cookie", help="Tools to inspect the Flask session cookie."
        )
        app.cli.add_command(cookie_cli)

        @cookie_cli.command("decode")
        @click.argument("cookie")
        def decode(cookie):
            """Decode a flask session cookie"""
            decoded_cookie = self.decode_cookie(cookie)
            click.echo(decoded_cookie)

        app.extensions["flask_cookie_decode"] = self

    def decode_cookie(self, cookie):
        """Decode a cookie by first checking the signature of the cookie. If
        the signature is valid, the cookie will be loaded and marked as "safe".
        If the signature is invalid, the cookie will be loaded but it will
        be marked as "unsafe".

        "Unsafe" here means that content of the cookie has not been signed by
        the correct secret key. That or the signature of the cookie itself is
        malformed or tampered with.
        """
        try:
            self._timestamp_signer.unsign(cookie, max_age=self._max_age)
        except SignatureExpired as expired:
            return ExpiredCookie(
                *self._unsafe_decode(cookie, date_signed=expired.date_signed)
            )
        except BadTimeSignature as bad_sign:
            return UntrustedCookie(
                *self._unsafe_decode(cookie, date_signed=bad_sign.date_signed)
            )
        return TrustedCookie(*self._safe_decode(cookie))

    def _safe_decode(self, cookie):
        """Validate the signature in the session cookie, decode the cookie
        payload and compute the expiration date based off of the Flask application
        instances PERMANENT_SESSION_LIFETIME config value.
        """
        contents, date_signed = self._signing_serializer.loads(
            cookie, return_timestamp=True
        )

        expires_at = (date_signed + timedelta(seconds=self._max_age)).isoformat()
        return (contents, expires_at)

    def _unsafe_decode(self, cookie, date_signed=None):
        """Ignoring the signature of the session cookies decode the cookies
        payload and the compute the expiration based off of the Flask application
        instances PERMANENT_SESSION_LIFETIME config value.

        The data loaded here is *untrusted*."""
        _, contents = self._signing_serializer.loads_unsafe(cookie)
        if date_signed is None:
            return (contents, None)

        try:
            expires_at = (
                datetime.utcfromtimestamp(date_signed)
                + timedelta(seconds=self._max_age)
            ).isoformat()
        except TypeError:
            expires_at = (date_signed + timedelta(seconds=self._max_age)).isoformat()

        return (contents, expires_at)
