# Database models for the application
from .extensions import db

from datetime import datetime,timezone

# to get current time in UTC Time zone -> datetime.now(timezone.utc)

# adm = Admin(full_name="Lakshya Bamne", user_name="Admin_lakshyaBamne", email="lakshyabamne181@gmail.com", contact="7024837727",password_hash="pbkdf2:sha256:600000$fhPpUD5qCyMdNuW8$6e7016d6b4a697721287e6fc0206588d6b8349f568b847a28a736921583e0074")
# Admin login details :-
# Username = Admin_lakshyaBamne
# Password = Password@ADMIN_69
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

    def __repr__(self):
        """
            Special method represents an object of Admin class when printed
        """
        return f'<Admin : {self.id} -> {self.user_name}>'

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
    email = db.Column(db.String(100), unique=True, nullable=False)
    contact = db.Column(db.String(15), unique=True, nullable=False)
    password_hash = db.Column(db.String(500))
    date_joined = db.Column(db.DateTime, default=datetime.now(timezone.utc)) # time when user signed up!

    def __repr__(self):
        """
            Special method represents an object of User class when printed
        """
        return f'<User : {self.id} -> {self.full_name} ({self.user_name})>'

class City(db.Model):
    """
        Cities where the users can be present
    """
    __tablename__ = "City"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """
            Special method represents an object of City class when printed
        """
        return f'<City : {self.id} -> {self.name}>'

class State(db.Model):
    """
        States where the users can be present
    """
    __tablename__ = "State"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """
            Special method represents an object of State class when printed
        """
        return f'<State : {self.id} -> {self.name}>'

class Country(db.Model):
    """
        Countries where the users can be present
    """
    __tablename__ = "Country"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """
            Special method represents an object of Country class when printed
        """
        return f'<Country : {self.id} -> {self.name}>'

class Location(db.Model):
    """
        Locations where the Store currently operates

        -> combination of City, State, Country
    """
    __tablename__ = "Location"

    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey("City.id"), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey("State.id"), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("Country.id"), nullable=False)

class PrimaryAddress(db.Model):
    """
        Intermediate table to connect Address table to Users
    """
    __tablename__ = "PrimaryAddress"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("Address.id"), nullable=False)

    def __repr__(self):
        """
            Special method represents an object of PrimaryAddress class when printed
        """
        return f'<PrimaryAddress : {self.user_id} -> {self.address_id}>'
    
class Address(db.Model):
    """
        Address table to store all the addresses of all users
    """
    __tablename__ = "Address"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))
    house_number = db.Column(db.String(50))
    line_1 = db.Column(db.String(200), nullable=False)
    line_2 = db.Column(db.String(200))
    pincode = db.Column(db.String(6), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey("Location.id"), nullable=False)

    def __repr__(self):
        """
            Special method represents an object of Address class when printed
        """
        return f'<Address : {self.id} -> {self.user_id}>'

class Category(db.Model):
    """
        Category of products available on the store
    """
    __tablename__ = "Category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))

    def __repr__(self):
        """
            Special method represents an object of Category class when printed
        """
        return f'<Category : {self.id} -> {self.name}>'

class Product(db.Model):
    """
        Products available on the store
    """
    __tablename__ = "Product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.Integer, db.ForeignKey("MeasurementUnit.id"), nullable=False)
    price_per_quantity = db.Column(db.Integer, nullable=False)
    seller = db.Column(db.Integer, db.ForeignKey("Seller.id"), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc)) # when was product added to store
    expiration_date = db.Column(db.DateTime, nullable=False)
    # create a one to many relationship to the rating table for every product
    rating = db.Column(db.Integer)

    def __repr__(self):
        """
            Special method represents an object of Product class when printed
        """
        return f'<Product : {self.id} -> {self.name}>'

class MeasurementUnit(db.Model):
    """
        Measurement units for the products on the store
    """
    __tablename__ = "MeasurementUnit"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    shorthand = db.Column(db.String(10), unique=True, nullable=True)

    def __repr__(self):
        """
            Measurement units for the products on the website
        """
        return f'<MeasurementUnit : {self.id} -> {self.name} ({self.shorthand})>'

class Rating(db.Model):
    """
        Ratings for all the products on the store
    """
    __tablename__ = "Rating"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("Product.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"), nullable=False)
    # individual ratings are shown on frontend by using query on this field
    stars = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc)) # used to show latest reviews
    description = db.Column(db.String(500))

    def __repr__(self):
        """
            Special method represents a rating for a product given by a registered user
        """
        return f'<Rating : {self.product_id} -> {self.stars}>'

class Seller(db.Model):
    """
        Sellers selling products in various categories to the store

        -> can be used in the future to add fucntionality where seller is contacted
        automatically when product goes out of stock
    """
    __tablename__ = "Seller"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    seller_contact = db.Column(db.String(20), nullable=False)
    seller_email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """
            Sellers for the products on the site
        """
        return f'<Seller : {self.id} -> {self.name}>'
    

