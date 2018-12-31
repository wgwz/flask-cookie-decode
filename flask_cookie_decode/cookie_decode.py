import click
from itsdangerous.exc import BadTimeSignature
from flask.cli import AppGroup
from flask.sessions import SecureCookieSessionInterface


class CookieDecode:
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
        """Initalizes the application with the extension.
        :param app: The Flask application object.
        """
        self.session_interface = SecureCookieSessionInterface()
        self.s = self.session_interface.get_signing_serializer(app)
        
        cookie_cli = AppGroup('cookie', help='Tools to inspect the Flask session cookie.')
        app.cli.add_command(cookie_cli)

        app.extensions['flask_cookie_decode'] = self

        @cookie_cli.command('decode')
        @click.option('--timestamp/--no-timestamp', default=False)
        @click.argument('cookie')
        def decode(cookie, timestamp):
            """Decode a flask session cookie"""
            try:
                click.echo(self.safe_decode(cookie, return_timestamp=timestamp))
            except BadTimeSignature as exc:
                click.echo(exc)
                click.echo(self.unsafe_decode(cookie))

    def safe_decode(self, cookie, return_timestamp=False):
        """"Validates the signature and loads session the cookie.
        
        Uses the underlying itsdangerous ``URLSafeTimedSerializer``"""
        return self.s.loads(cookie, return_timestamp=return_timestamp)

    def unsafe_decode(self, cookie):
        """"Loads the session cookie even if the signature is invalid."""
        is_safe, contents = self.s.loads_unsafe(cookie)
        return contents

