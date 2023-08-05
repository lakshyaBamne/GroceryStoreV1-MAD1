from flask import Blueprint

bp = Blueprint('user', __name__)

from flaskr.user import (
    userpage,
    user_actions
)