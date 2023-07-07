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

class Admin(db.Model):
    """
        Admin Table

        - Stores the information about an admin of the store
    """

    __tablename__ = "Admin"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    user_name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    contact = db.Column(db.String(15), unique=True)
    password_hash = db.Column(db.String(500))

# adm = Admin(full_name="Lakshya Bamne", user_name="Admin_lakshyaBamne", email="lakshyabamne181@gmail.com", contact="7024837727",password_hash="pbkdf2:sha256:600000$fhPpUD5qCyMdNuW8$6e7016d6b4a697721287e6fc0206588d6b8349f568b847a28a736921583e0074")
# Admin login details :-
# Username = Admin_lakshyaBamne
# Password = Password@ADMIN_69