from flask import Flask
from main.controllers import blueprints_ctrl
from main.database.models.database import engine
from sqlmodel import SQLModel


def create_app(test_config=None):
    app = Flask(
        __name__,
        static_url_path="/static",
        static_folder="static",
        instance_relative_config=True,
    )

    app.config.from_mapping(
        SECRET_KEY="super secret key",
        SESSION_TYPE="filesystem",
        JSONIFY_PRETTYPRINT_REGULAR=False,
    )

    # add routes
    for bp in blueprints_ctrl:
        app.register_blueprint(bp)

    # create database
    with app.app_context():
        SQLModel.metadata.create_all(engine)

    return app
