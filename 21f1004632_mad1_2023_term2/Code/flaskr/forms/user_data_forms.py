# Module to contain all the important authentication related forms

from flask_wtf import FlaskForm

from wtforms import ( 
    StringField,
    PasswordField, 
    SubmitField, 
    EmailField, 
    IntegerField
)

from wtforms.validators import (
    DataRequired
)

