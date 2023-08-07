# routes for various actions which the user can make

from flask import (
    request,
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
@bp.route("/user/add_to_cart/<username>/<int:product_id>", methods=["POST"])
def add_to_cart(username,product_id):
    """
        Add a product with the given product id to the cart of the user
    """

    if request.method == "POST":
        # we need to extract the quantity from the form which the user submitted

        quantity = request.form.get('quantity')

        if not quantity:
            quantity = 1

        cart_obj = Cart(username=username, product=product_id, quantity=quantity)

        db.session.add(cart_obj)
        db.session.commit()

        print(f"__LOG__ Added product : {product_id}({quantity}) to cart of user : {username}")
        flash("__LOG__ Successfully added product to cart", "SUCCESS")

        return redirect(url_for("user.user_page", username=username))

@bp.route("/user/remove_from_cart/<username>/<int:product_id>", methods=["GET","POST"])
def remove_from_cart(username, product_id):
    """
        Remove a product from the user cart with the given product id
    """
    to_delete = Cart.query.filter_by(username=username, product=product_id).all()

    for item in to_delete:
        db.session.delete(item)

    db.session.commit()

    print(f"__LOG__ Removed product : {product_id} to cart of user : {username}")
    flash("__LOG__ Successfully removed product from cart", "SUCCESS")

    return redirect(url_for("user.user_cart", username=username))

