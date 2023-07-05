from flask import render_template, jsonify, Blueprint

bp = Blueprint(
    "index",
    __name__,
    template_folder="templates",
)


class IndexCtrl:
    @bp.route("/", methods=["GET"])
    def inicial_template():
        return render_template(
            template_name_or_list="index.html",
            titulo="index",
        )

    @bp.route("/json", methods=["GET"])
    def inicial_json():
        return jsonify({"pagina": "inicial"})
