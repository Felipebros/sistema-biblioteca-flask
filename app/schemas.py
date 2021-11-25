from flask_marshmallow import Marshmallow
from .model import Obra, Autor

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class AutorSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = Autor
        load_instance = True

    id = ma.auto_field(dump_only=True)


class ObraSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Obra
        load_instance = True
        include_fk = True

    id = ma.auto_field(dump_only=True)
    autores = ma.Nested(AutorSchema, many=True)
