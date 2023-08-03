# Module to contain all the important authentication related forms

from flask_wtf import FlaskForm

from wtforms import ( 
    StringField,
    PasswordField, 
    SubmitField, 
    EmailField, 
    IntegerField,
    SelectField,
    TextAreaField,
    DateField,
    DateTimeLocalField
)

from wtforms.validators import (
    DataRequired
)

class LocationForm(FlaskForm):
    """
        Admin Data Form to add a new location where the web store operates

        -> Updation and Deletion facility will be provided in the Accordion in the main content

        -> Also to make changes to the database, system asks for the Admin password
        in the form itself
    """
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SellerForm(FlaskForm):
    """
        Admin Data Form to add a new Seller/Brand to the web store

        -> Admin Password is required in the form itself to make changes to the databse
    """
    name = StringField('Seller Name', validators=[DataRequired()])
    contact = StringField('Contact', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Unit(FlaskForm):
    """
        Admin Data Form to add a new Measurement Unit for products

        -> Admin password is required in the form itself to make changes to the database
    """
    name = StringField('Unit Name', validators=[DataRequired()])
    shorthand = StringField('Shorthand', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    """
        Admin Data Form to add a new Category to the Database
    """
    name = StringField('Category Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ProductForm(FlaskForm):
    """
        Admin Data Form to add a new Product to the Database
    """
    name = StringField('Product Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    category = StringField('Category', validators=[DataRequired()])
    quantity = IntegerField('Available Quantity', validators=[DataRequired()])
    unit = StringField('Unit of Measurement', validators=[DataRequired()])
    price_per_quantity = IntegerField('Price', validators=[DataRequired()])
    seller = StringField('Seller', validators=[DataRequired()])
    expiration_date = DateField('Expiration Date', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


