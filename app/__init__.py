import os

from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_marshmallow


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    config_db(app)
    config_marshmallow(app)

    Migrate(app, app.db)

    from .obras import bp_obras
    app.register_blueprint(bp_obras)

    return app
