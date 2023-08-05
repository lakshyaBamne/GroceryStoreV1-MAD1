# routes for various actions which the user can make

from flask import (
    session,
    flash,
    url_for,
    redirect
)

from flaskr.user import bp

from flaskr.extensions import db

from flaskr.models import (
    User,
    Cart,
    SaveForLater
)

# cart_object=Cart(username="lakshyaBamne", product=1)
@bp.route("/user/add_to_cart/<username>/<int:product_id>", methods=["GET", "POST"])
def add_to_cart(username,product_id):
    """
        Add a product with the given product id to the cart of the user
    """
    cart_obj = Cart(username=username, product=product_id)

    db.session.add(cart_obj)
    db.session.commit()

    print(f"__LOG__ Added product : {product_id} to cart of user : {username}")
    flash("__LOG__ Successfully added product to cart", "SUCCESS")

    return redirect(url_for("user.user_page", username=username))