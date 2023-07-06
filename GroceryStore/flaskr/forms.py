from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired

class SignupForm(FlaskForm):
    """
        Sign Up form
    """
    name = StringField('Full Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password_hash = StringField('Password Hash', validators=[DataRequired()])
    contact = StringField('Contact', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class SigninForm(FlaskForm):
    """
        Sign In form
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

