from flask import Blueprint, current_app, request, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound
from .model import Obra, Autor
from .schemas import AutorSchema, ObraSchema


bp_obras = Blueprint('obras', __name__)


@bp_obras.route('/obras', methods=['POST'])
def cadastrar():
    autor_schema = AutorSchema()
    obra_schema = ObraSchema()

    json_data = request.json
    if not json_data:
        return jsonify({'messagem': 'Nenhum dado de entrada fornecido'}), 400

    data_autores = dict(nomes=json_data['autores'])
    del json_data['autores']

    try:
        data_obra = obra_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422

    obra = Obra.query.filter_by(titulo=json_data['titulo']).first()
    if obra:
        return jsonify({'messagem': 'Obra já cadastrada com esse título'}), 422

    current_app.db.session.add(data_obra)

    for data_autor in data_autores['nomes']:
        try:
            data_autor = autor_schema.load(dict(nome=data_autor))
        except ValidationError as err:
            return err.messages, 422

        autor = Autor.query.filter_by(nome=data_autor.nome).first()
        if autor:
            return jsonify({'messagem': f'Autor já cadastrado com esse nome "{data_autor.nome}"'}), 422

        autor = Autor(nome=data_autor.nome, obra_id=data_obra.id)
        current_app.db.session.add(autor)

    current_app.db.session.commit()

    obra_result = obra_schema.dump(Obra.query.get(data_obra.id))

    return obra_schema.jsonify(obra_result), 201


@bp_obras.route('/upload-obras', methods=['POST'])
def cadastrar_csv():
    ...


@bp_obras.route('/obras', methods=['GET'])
def listar():
    obra_schema = ObraSchema(many=True)
    result = Obra.query.all()
    return obra_schema.jsonify(result), 200


@bp_obras.route('/obras/<int:id>', methods=['PUT'])
def modificar(id):
    obra_schema = ObraSchema(many=True)
    autor_schema = AutorSchema(many=True)

    try:
        obra = Obra.query.filter(Obra.id == id).one()
    except NoResultFound:
        return jsonify({'mensagem': 'Obra não encontrada.'}), 400

    obra_result = obra_schema.dump(obra)
    autor_result = autor_schema.dump(obra.quotes.all())
    return jsonify({'obra': obra_result, 'autores': autor_result}), 200


@bp_obras.route('/obras/<int:id>', methods=['DELETE'])
def deletar():
    Obra.query.filter(Obra.id == id).delete()
    current_app.db.session.commit()
    return jsonify({'Deletado'})


@bp_obras.route('/file-obras', methods=['POST'])
def enviar_email():
    ...
