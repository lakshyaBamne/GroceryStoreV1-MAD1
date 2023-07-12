# Module to contain all the important authentication related forms

from flask_wtf import FlaskForm

from wtforms import ( 
    StringField,
    PasswordField, 
    SubmitField, 
    EmailField, 
    IntegerField,
    SelectField
)

from wtforms.validators import (
    DataRequired
)

class LocationForm(FlaskForm):
    """
        Admin Data Form to add a new location where the web store operates

        -> The state and country fields here generate data dynamically
        -> but the Admin can create a new state and country if he so desires
        -> thus validation for these fields should not be checked

        -> Also to make changes to the database, system asks for the Admin password
        in the form itself
    """
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


