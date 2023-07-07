from flask import (
    render_template,
    request,
    url_for,
    flash,
    redirect
)

from flaskr.admin import bp

@bp.route("/admin/<username>", methods=["GET", "POST"])
def admin(username):
    """
        Admin page handler
    """
    if request.method == "GET":
        return render_template("admin/admin_index.html", username=username)
    elif request.method == "POST":
        pass