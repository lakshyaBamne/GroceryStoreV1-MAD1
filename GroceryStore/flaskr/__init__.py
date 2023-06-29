from flask import Flask

from flaskr.main import bp as app_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(app_bp)

    return app