from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Obras(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    editora = db.Column(db.String(255))
    foto = db.Column(db.Text())
    autores = db.Column(db.Text())
