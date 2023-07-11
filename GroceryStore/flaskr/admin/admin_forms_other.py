from flask import (
    render_template
)

from flaskr.admin import bp

@bp.route("/admin/forms/unit", methods=["GET", "POST"])
def admin_form_unit():
    """
        Admin dashboard handler for Form-Adding a unit of measurement
    """
