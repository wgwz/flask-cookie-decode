from flask import Flask, jsonify, session, request
from flask_cookie_decode import CookieDecode

app = Flask(__name__)
app.config.update({'SECRET_KEY': 'jlghasdghasdhgahsdg'})
flask_decode = CookieDecode()
flask_decode.init_app(app)

@app.route('/')
def index():
    a = request.args.get('a')
    session['a'] = a
    return jsonify(dict(session))
