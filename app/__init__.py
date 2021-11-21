import os

from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    config_db(app)

    Migrate(app, app.db)

    return app
