# Flask objects and methods import
from flask import Flask

# Configuration object import
from config import Config, Development

# Extension imports
from .extensions import *

# Blueprint Imports
from flaskr.main import bp as app_bp
from flaskr.auth import bp as auth_bp
from flaskr.user import bp as user_bp
from flaskr.admin import bp as admin_bp

def create_app():
    # application instance is created inside the Application Factory
    app = Flask(__name__)

    # Configurations for the web application
    app.config.from_object(Development)

    # initializing the extension objects for this application instance
    db.init_app(app)

    # create the database models after configuring the database object
    with app.app_context():
        db.create_all()

    migrate.init_app(app, db)

    # Blueprint registrations
    app.register_blueprint(app_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)

    return app