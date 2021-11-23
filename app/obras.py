from flask import Blueprint, current_app, request, jsonify
from marshmallow import ValidationError
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

    data_autores = dict(nome=json_data['autores'].copy())
    # data_autores = json_data['autores'].copy()
    del json_data['autores']

    # try:
    #     data = autor_schema.load(json_data)
    # except ValidationError as err:
    #     return err.messages, 422

    # import ipdb; ipdb.set_trace()

    obra = Obra.query.filter_by(titulo=json_data['titulo']).first()
    if obra is None:
        obra = obra_schema.load(json_data)
        current_app.db.session.add(obra)

    for data_autor in data_autores['nome']:
        autor = Autor.query.filter_by(nome=data_autor).first()
        if autor is None:
            autor = Autor(nome=data_autor, obra_id=obra.id)
            current_app.db.session.add(autor)

    # data_autores['obra_id'] = autores
    # autores = autor_schema.load({'nome': 'autor 1'})
    # autor = Autor(nome='Au?tor 1', obra=obra)

    current_app.db.session.add(autor)
    current_app.db.session.commit()

    obra_result = obra_schema.dump(Obra.query.get(obra.id))
    # autor_result = Autor.query.filter_by(obra_id=obra.id).all()
    # import ipdb; ipdb.set_trace()
    # result = {**obra_result, **autor_result}

    return obra_schema.jsonify(obra_result), 201


@bp_obras.route('/upload-obras', methods=['POST'])
def cadastrar_csv():
    ...


@bp_obras.route('/obras', methods=['GET'])
def mostrar():
    obra_schema = ObraSchema(many=True)
    result = Obras.query.all()
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
    return jsonify({'obra': obra_result, 'autores':
    autor_result}), 200


@bp_obras.route('/obras/<int:id>', methods=['DELETE'])
def deletar():
    Obras.query.filter(Obra.id == id).delete()
    current_app.db.session.commit()
    return jsonify({'Deletado'})


@bp_obras.route('/file-obras', methods=['POST'])
def enviar_email():
    ...
