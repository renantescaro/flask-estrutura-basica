from flask import Flask
from flaskr.controllers.inicial_ctrl import bp as bp_inicial

def create_app(test_config=None):
    app = Flask(
        __name__,
        static_url_path = '/static',
        static_folder   = 'static',
        instance_relative_config = True )

    app.config.from_mapping(
        SECRET_KEY   = 'super secret key',
        SESSION_TYPE = 'filesystem',
        JSONIFY_PRETTYPRINT_REGULAR = False )


    # adicionar rotas
    app.register_blueprint(bp_inicial)
    return app