from flask import render_template
from flaskr.auth import bp

@bp.route("/signin", methods=["GET", "POST"])
def signin():
    return render_template("auth/signin.html")