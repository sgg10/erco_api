from flask import Flask

from .db import data


def create_app():
    app = Flask(__name__)
    app.register_blueprint(data)
    return app
