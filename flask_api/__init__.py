import config
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    template_dir = "../template"
    app = Flask(
        __name__,
        static_url_path="",
        static_folder="../static",
        template_folder=template_dir,
    )
    environment_configuration = os.environ["CONFIGURATION_SETUP"]

    app.config.from_object(environment_configuration)

    db.init_app(app)

    with app.app_context():
        from .dog_api import dog_api_bp

        db.create_all()

        app.register_blueprint(dog_api_bp)
        return app
