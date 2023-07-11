from flask import (
    render_template
)

from flaskr.admin import bp

@bp.route("/admin/forms/city", methods=["GET", "POST"])
def admin_form_city():
    """
        Admin dashboard handler for Form-Adding a City
    """

@bp.route("/admin/forms/state", methods=["GET", "POST"])
def admin_form_state():
    """
        Admin dashboard handler for Form-Adding a State
    """

@bp.route("/admin/forms/country", methods=["GET", "POST"])
def admin_form_country():
    """
        Admin dashboard handler for Form-Adding a Country
    """