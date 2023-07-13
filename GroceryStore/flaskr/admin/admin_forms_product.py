from flask import (
    request,
    session,
    redirect,
    url_for,
    flash,
    render_template
)

from flaskr.admin import bp

from werkzeug.security import check_password_hash

from flaskr.models import (
    Admin,
    Product,
    Category
)
from flaskr.extensions import db
from flaskr.forms.admin_data_forms import (
    CategoryForm,
    ProductForm
)

# we make different routed for the different forms in the Admin Dashboard

@bp.route("/admin/forms/category", methods=["GET", "POST"])
def admin_form_category():
    """
        Admin dashboard handler for Form-Adding a new category
    """

    if request.method == "POST":
        flash(f"__LOG__ Post request successfull at /admin/forms/category ...", "SUCCESS")
        return redirect(url_for("admin.admin", username=session['Username']))


@bp.route("/admin/forms/product", methods=["GET", "POST"])
def admin_form_product():
    """
        Admin dashboard handler for Form-Adding a new product
    """