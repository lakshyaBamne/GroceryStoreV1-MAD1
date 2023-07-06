from flask import render_template, request, redirect, url_for

from flaskr.auth import bp
from flaskr.forms import SigninForm


@bp.route("/signin", methods=["GET", "POST"])
def signin():
    # handling a Sign in from user... to be changed using sessions and database authentication
    if request.method == 'POST':
        username = request.form.get('username')
        return redirect(url_for('user.user_page', username=username))

    form = SigninForm()
    return render_template("auth/signin.html", form=form)