from flask import Blueprint, render_template

bp = Blueprint("auth", __name__)

from flaskr.auth import signup, signin