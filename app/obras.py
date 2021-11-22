from flask import Blueprint, current_app, request, jsonify
from .model import Obras
from .schemas import AutoresSchema, ObrasSchema


bp_obras = Blueprint('obras', __name__)


@bp_obras.route('/obras', methods=['POST'])
def cadastrar():
    autores_schema = AutoresSchema()
    obras_schema = ObrasSchema()
    obra = obras_schema.load(request.json)
    current_app.db.session.add(obra)
    current_app.db.session.commit()
    return obras_schema.jsonify(obra), 201


@bp_obras.route('/upload-obras', methods=['POST'])
def cadastrar_csv():
    ...


@bp_obras.route('/obras', methods=['GET'])
def mostrar():
    obras_schema = ObrasSchema(many=True)
    result = Obras.query.all()
    return obras_schema.jsonify(result), 200


@bp_obras.route('/obras/<int:id>', methods=['PUT'])
def modificar():
    ...


@bp_obras.route('/obras/<int:id>', methods=['DELETE'])
def deletar():
    Obras.query.filter(Obras.id == id).delete()
    current_app.db.session.commit()
    return jsonify({'Deletado'})


@bp_obras.route('/file-obras', methods=['POST'])
def enviar_email():
    ...
