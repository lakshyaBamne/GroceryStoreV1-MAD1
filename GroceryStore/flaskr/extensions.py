# Extension file to store all the flask-extension imports 
# and instantiations
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()