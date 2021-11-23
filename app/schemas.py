# from marshmallow import fields
from flask_marshmallow import Marshmallow
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .model import Obra, Autor

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class AutorSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = Autor
        load_instance = True


class ObraSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Obra
        load_instance = True
        include_fk = True
        transient = True

    autores = ma.Nested(AutorSchema)

    # links = ma.Hyperlinks({
    #     'self': ma.URLFor('detalhe_obra', values=dict(id='<id>')),
    #     'collection': ma.URLFor('lista_obra')
    # })
    # autores = ma.List(ma.HyperlinkRelated('obras'))

    # autores = ma.Nested(this, default=[], many=True)
    # autores = ma.Nested("ClientSiteSchema", default=[], many=True)
    # autores = ma.URLFor(AutoresSchema)
    # autores = ma.String(many=True)
    # autores = ma.List(ma.HyperlinkRelated('autores'))
