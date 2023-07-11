from flask import render_template, jsonify, Blueprint

bp = Blueprint(
    "index",
    __name__,
    template_folder="templates",
)


class IndexCtrl:
    @bp.route("/json", methods=["GET"])
    def inicial_json():
        return jsonify({"pagina": "inicial"})
