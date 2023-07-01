from flask import render_template
from flaskr.auth import bp

@bp.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("auth/signup.html")