from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Obra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), unique=True, nullable=False)
    editora = db.Column(db.String(255))
    foto = db.Column(db.Text())


class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    obra_id = db.Column(db.Integer, db.ForeignKey('obra.id'))
    obra = db.relationship('Obra', backref=db.backref('autores', cascade='all, delete-orphan'))
