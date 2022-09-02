from flask import Blueprint

dog_api_bp = Blueprint('dog_api', __name__)

from . import routes
