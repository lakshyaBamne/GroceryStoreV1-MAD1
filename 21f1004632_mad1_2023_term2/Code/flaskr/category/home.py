# routes for the category pages

from flask import (
    session,
    url_for,
    render_template,
    redirect
)

from flaskr.category import bp

from flaskr.models import (
    Cart,
    SaveForLater,
    Product,
    Category
)

from flaskr.extensions import db

@bp.route("/category/<int:id>")
def category_home(id):
    """
        view function to show the home page of categories to a user
    """
    data={}

    # first we need to collect the data to be passed to a category page
    # we need all the product information for the given product
    all_products = Product.query.filter_by(category=id).order_by(Product.expiration_date).all()

    category = Category.query.filter_by(id=id).first()

    data[f"products"] = all_products
    data[f"category"] = category

    if 'Username' in session:
        return render_template("category/category_home.html", username=session['Username'],data=data)
    else:
        return "<h1>Please sign in to browse the products in categories!</h1>"

