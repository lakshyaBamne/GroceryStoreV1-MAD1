
from flaskr.models import (
    User,
    Cart,
    SaveForLater,
    Product
)

def get_user_data(username):
    """
        Function to get a user's data for the user's profile page
    """
    user = User.query.filter_by(user_name=username).first()

    result={}

    result["id"] = user.id
    result["name"] = user.full_name
    result["username"] = user.user_name
    result["email"] = user.email
    result["contact"] = user.contact
    result["joined"] = user.date_joined

    return result

def get_cart_items(username):
    """
        Function to get all the items stored in cart for the given user
    """


