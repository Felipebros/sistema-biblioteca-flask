from flask_marshmallow import Marshmallow
from .model import Obras

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class ObrasSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Obras
        load_instance = True
