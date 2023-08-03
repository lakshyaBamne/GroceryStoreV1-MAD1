#routes to take care of actions like delete and edit on the admin page

from flask import (
    session,
    flash,
    url_for,
    redirect
)

from flaskr.admin import bp

from flaskr.extensions import db

from flaskr.models import (
    Category,
    Product,
    Location
)

@bp.route("/admin/actions/delete/category/<int:id>")
def action_delete_category(id):
    """
        Endpoint to delete a category from the database when admin clicks a button
    """
    # delete the category from the database with given id
    to_delete = Category.query.get(id)

    db.session.delete(to_delete)
    db.session.commit()

    flash(f"__LOG__ [DELETE] successfully deleted category : {to_delete.id} -> {to_delete.name}", "SUCCESS")
    print(f"__LOG__ [DELETE] successfully deleted a category")
    return redirect(url_for("admin.admin", username=session["Username"]))

@bp.route("/admin/actions/delete/product/<int:id>")
def action_delete_product(id):
    """
        Endpoint to delete a product from the database when admin clicks a button
    """
    # delete the product from the database with the given id
    to_delete = Product.query.get(id)

    db.session.delete(to_delete)
    db.session.commit()

    flash(f"__LOG__ [DELETE] successfully deleted product : {to_delete.id} -> {to_delete.name}", "SUCCESS")
    print(f"__LOG__ [DELETE] successfully deleted a product")
    return redirect(url_for("admin.admin", username=session["Username"]))

@bp.route("/admin/actions/delete/location/<int:id>")
def action_delete_location(id):
    """
        Endpoint to delete a Store location from the database when admin clicks a button
    """
    # delete the product from the database with the given id
    to_delete = Location.query.get(id)

    db.session.delete(to_delete)
    db.session.commit()

    flash(f"__LOG__ [DELETE] successfully deleted store location : {to_delete.id}", "SUCCESS")
    print(f"__LOG__ [DELETE] successfully deleted a store location")
    return redirect(url_for("admin.admin", username=session["Username"]))

