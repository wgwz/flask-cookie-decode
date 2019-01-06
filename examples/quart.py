from quart import Quart, jsonify, session, request
from flask_cookie_decode import CookieDecode

app = Quart(__name__)
app.config.update(
    {"SECRET_KEY": "jlghasdghasdhgahsdg", "PERMANENT_SESSION_LIFETIME": 3600}
)
flask_decode = CookieDecode()
flask_decode.init_app(app)

@app.route('/')
async def index():
    a = request.args.get("a")
    session["a"] = a
    return jsonify(dict(session))
