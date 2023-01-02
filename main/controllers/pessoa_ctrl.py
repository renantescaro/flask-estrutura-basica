from flask import jsonify, Blueprint, abort, request

from main.database.models.pessoa_model import Pessoa
from main.database.models.database import run_query, run_insert, select

bp = Blueprint(
    'pessoa',
    __name__,
    template_folder='templates' 
)

class PessoaCtrl:
    @bp.route('/pessoa', methods=['GET'])
    def consultar_pessoa():
        statement = select(Pessoa).where(Pessoa.nome == 'renan')
        pessoa:Pessoa = run_query(statement)
        if pessoa is not None:
            return jsonify({
                'nome':pessoa.nome,
                'genero':pessoa.genero.value if pessoa.genero else '',
            })
        return abort(404)

    @bp.route('/pessoa', methods=['POST'])
    def nova_pessoa():
        try:
            if data := request.json:
                pessoa = Pessoa(
                    nome=data['nome'],
                    pronome=data['pronome'],
                    peso=data['peso'],
                    genero=data['genero'],
                    data_nascimento=data['data_nascimento'],
                )
                run_insert(pessoa)
                return jsonify({})

        except Exception as e:
            print(e)

        return abort(400)
