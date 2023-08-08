# Utility module contains functions to get data from the database
# all the results are returned as a List of dictionaries
# where each element of the list will be a dictionary object containing
# the required attributes for different entities

from flaskr.models import (
    Category,
    Product,
    Location,
    City,
    State,
    Country,
    MeasurementUnit,
    Seller,
)

from flaskr.extensions import db

def get_categories():
    """
        Function to get the categories present in the database
    """    
    result = []
    all_categories = Category.query.order_by(Category.name).all()

    for i in range(len(all_categories)):
        cat_id = all_categories[i].id
        cat_name = all_categories[i].name
        cat_desc = all_categories[i].description

        result_object = {
            "id" : cat_id,
            "name" : cat_name,
            "description" : cat_desc
        }

        result.append(result_object)

    return result

def get_products():
    """
        Function to get the products present in the database
    """
    result = []
    all_products = Product.query.order_by(Product.category).all()

    for i in range(len(all_products)):
        prod_id = all_products[i].id
        prod_name = all_products[i].name
        prod_desc = all_products[i].description
        prod_price = all_products[i].price_per_quantity

        result_object = {
            "id" : prod_id,
            "name" : prod_name,
            "description" : prod_desc,
            "price" : prod_price
        }

        result.append(result_object)

    return result

def get_locations():
    """
        Function to get the current Store locations
    """
    result = []
    all_locations = Location.query.order_by(Location.id).all()

    all_cities = City.query.order_by(City.id).all()
    all_states = State.query.order_by(State.id).all()
    all_countries = Country.query.order_by(Country.id).all()

    for i in range(len(all_locations)):
        location_id = all_locations[i].id
        city_name = [city.name for city in all_cities if city.id is all_locations[i].city_id]
        state_name = [state.name for state in all_states if state.id is all_locations[i].state_id]
        country_name = [country.name for country in all_countries if country.id is all_locations[i].country_id]

        result_object = {
            "id" : location_id,
            "city" : city_name[0],
            "state" : state_name[0],
            "country" : country_name[0]
        }

        result.append(result_object)

    return result

def get_units():
    """
        Function to get the units of measurements
    """
    result = []
    all_units = MeasurementUnit.query.order_by(MeasurementUnit.id).all()

    for i in range(len(all_units)):
        unit_id = all_units[i].id
        unit_name = all_units[i].name
        unit_shorthand = all_units[i].shorthand

        result_object = {
            "id" : unit_id,
            "name" : unit_name,
            "shorthand" : unit_shorthand
        }

        result.append(result_object)

    return result

def get_sellers():
    """
        Function to get the sellers for the store
    """
    result = []
    all_seller = Seller.query.order_by(Seller.id).all()

    for i in range(len(all_seller)):
        seller_id = all_seller[i].id
        seller_name = all_seller[i].name
        seller_contact = all_seller[i].seller_contact
        seller_email = all_seller[i].seller_email

        result_object = {
            "id" : seller_id,
            "name" : seller_name,
            "contact" : seller_contact,
            "email" : seller_email
        }

        result.append(result_object)

    return result


