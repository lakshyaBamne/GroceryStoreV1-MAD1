from flask import Blueprint

bp = Blueprint('category', __name__)

from flaskr.category import home