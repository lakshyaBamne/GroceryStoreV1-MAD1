from flask import render_template, session,redirect, url_for

from flaskr.main import bp

@bp.route("/", methods=["GET"])
def index():
    if 'Username' in session:
        # if user is present in the session => has not log out
        # clicking on the index page button will redirect to
        # home page of the user
        return redirect(url_for('user.user_page', username=session['Username']))

    return render_template("main/index.html")