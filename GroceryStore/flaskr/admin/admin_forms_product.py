from flask import (
    render_template
)

from flaskr.admin import bp

# we make different routed for the different forms in the Admin Dashboard

@bp.route("/admin/forms/category", methods=["GET", "POST"])
def admin_form_category():
    """
        Admin dashboard handler for Form-Adding a new category
    """

@bp.route("/admin/forms/product", methods=["GET", "POST"])
def admin_form_product():
    """
        Admin dashboard handler for Form-Adding a new product
    """

@bp.route("/admin/forms/seller", methods=["GET", "POST"])
def admin_form_seller():
    """
        Admin dashboard handler for Form-Adding a new Seller
    """