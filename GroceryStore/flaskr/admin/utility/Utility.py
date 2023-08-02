# Utility module contains functions to get data from the database
# all the results are returned as a List of dictionaries
# where each element of the list will be a dictionary object containing
# the required attributes for different entities

from flask import jsonify

from flaskr.models import Category

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
