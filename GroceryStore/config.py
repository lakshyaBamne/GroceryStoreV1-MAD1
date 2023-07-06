# Flask configuration classes for the web-application

import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    """
        Base confoguration class for the aplication

        -> If we require more than one configurations for our application
        we simple make classes that inherit from this base class

        -> A configuration variable's value is always preferred to come from
        the environment in which the web app is runing, thus the given format is adopted
    """

    # most important flask configuration variable used by different flask-extensions
    # for different purposes like generating signatures or tokens

    # Flask-WTF : uses it to protect web forms against CSRF attacks (Cross-Site-Request-Forgery)
    # Sessions : use this secret key to cryptographically-sign cookies sent to clients

    # To generate a good random secret key string run the following two commands in a python interpreter:-
    # $ import secrets
    # $ secrets.token_urlsafe(16)
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1EZKpnQcRzHdR9wHLy7GYw'

class Development(Config):
    """
        Development Configuration class

        -> sqlite database is used in the development environment
    """

    # Flask-SQLAlchemy configuration variable

    # this variable is used to get the location of the application database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')

    # this modification stops the Flask-SQLAlchemy from sending signals to
    # the application everytime a change is about to be made in the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False