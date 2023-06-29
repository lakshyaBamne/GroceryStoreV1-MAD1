from flask import Blueprint

bp = Blueprint("app", __name__)

from flaskr.main import routes