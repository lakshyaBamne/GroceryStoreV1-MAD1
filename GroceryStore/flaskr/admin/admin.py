from flask import (
    render_template,
    request,
    url_for,
    flash,
    redirect
)

from flaskr.admin import bp

@bp.route("/admin", methods=["GET", "POST"])
def admin():
    """
        Admin page handler
    """
    if request.method == "GET":
        return render_template("admin/admin_index.html")
    elif request.method == "POST":
        pass