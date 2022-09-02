import config
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']

    app.config.from_object(environment_configuration)

    db.init_app(app)

    with app.app_context():
        from .dog_api import dog_api_bp

        db.create_all()

        app.register_blueprint(dog_api_bp)
        return app
    


