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


class Autores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    obras_id = db.Column(db.Integer, db.ForeignKey('obras.id'))
    autores = db.relationship('Obras', backref='autores')
