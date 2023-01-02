from flask import render_template, jsonify, Blueprint

bp = Blueprint(
    'inical',
    __name__,
    template_folder='templates' 
)

class InicialCtrl:
    @bp.route('/', methods=['GET'])
    def inicial_template():
        return render_template(
            template_name_or_list='inicial.html',
            titulo='inicial'
        )

    @bp.route('/json', methods=['GET'])
    def inicial_json():
        return jsonify({'pagina':'inicial'})
