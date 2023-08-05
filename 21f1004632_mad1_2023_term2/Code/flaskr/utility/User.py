
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

    # first extract all the items from the cart for the username
    result = []

    all_items = Cart.query.filter_by(username=username).all() # list of items in cart
    all_products = Product.query.all() # list of products
    
    for i in range(len(all_items)):
        prod_data = None
        for item in all_products:
            if item.id is all_items[i].product:
                prod_data = item

        product_data = {
            "name" : prod_data.name,
            "description" : prod_data.description,
            "price" : prod_data.price_per_quantity,
            "seller" : prod_data.seller
        }


        result_object = {
            "product_id" : all_items[i].product,
            "quantity" : all_items[i].quantity,
            "product_data" : product_data
        }

        result.append(result_object)

    return result
    





