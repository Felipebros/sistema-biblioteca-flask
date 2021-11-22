from flask_marshmallow import Marshmallow
from .model import Obras, Autores

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class ObrasSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Obras
        load_instance = True


class AutoresSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = Autores
        load_instance = True
        include_fk = True
