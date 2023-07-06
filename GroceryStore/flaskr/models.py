# Database models for the application
from .extensions import db

class User(db.Model):
    """
        User Table

        - Stores Signin information about a user
        - Used in other tables to associate a User with various 
        other information
    """
    # since flask-migrate uses a snake case to store all table names
    # we should specify a name if we want that to be overridden
    __tablename__ = "User"

    # SQLAlchemy will automatically set the first Integer Primary Key
    # column that is not marked a Foreign Key as autoincrement
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    user_name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100))
    contact = db.Column(db.String(15))
    password_hash = db.Column(db.String(500))

    def __repr__(self):
        """
            Special method represents an object of this class when printed
        """
        return f'<User {self.id}, {self.user_name}>'



