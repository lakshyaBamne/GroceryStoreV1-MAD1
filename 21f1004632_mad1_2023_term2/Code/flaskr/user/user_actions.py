# routes for various actions which the user can make

from flask import (
    request,
    session,
    flash,
    url_for,
    redirect,
    render_template
)

from flaskr.user import bp

from flaskr.extensions import db

from flaskr.models import (
    User,
    Cart,
    SaveForLater
)

from flaskr.utility.User import clear_cart

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


@bp.route("/user/checkout/<username>", methods=["GET"])
def checkout(username):
    """
        Proceed to check out
    """
    if 'Username' in session:
        # proceed to check out page after removing items from the cart
        clear_cart(username)

        flash(f"__LOG__ Successfull checkout for {username}", "SUCCESS")
        print(f"__LOG__ Successfull checkout for {username}", "SUCCESS")

        return render_template("user/checkout.html"), {"Refresh" : f"2, url={url_for('user.user_page', username=username)}"}

        # return redirect(url_for('user.user_page', username=username))
    else:
        print(f"__LOG__ [POSSIBLE BREACH] someone tried to access account of {username}")
        return "<h1>Nice try hacker!! your tricks not working on this website</h1>"
