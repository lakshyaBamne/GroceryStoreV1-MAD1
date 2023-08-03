from flask import (
    render_template,
    request, 
    redirect, 
    url_for,
    flash,
    session
)

from werkzeug.security import check_password_hash

from flaskr.auth import bp
from flaskr.forms.auth_forms import SigninForm
from flaskr.models import User

@bp.route("/signin", methods=["GET", "POST"])
def signin():
    form = SigninForm()
    
    if request.method == 'GET':
        return render_template("auth/signin.html", form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            # if user submits the form with all validators, we need to authenticate the user
            user_data = request.form

            username = user_data['username']

            # we need to get the stored hash in the database to validate the password
            db_data = User.query.filter_by(user_name=username).first()

            if db_data is None:
                # given user does not exist
                flash(f"A user with the given username DOES NOT EXIST!! Try again.", "ERROR")
                return render_template("auth/signin.html", form=form)
            else:
                # a user with the given username EXISTS in the database

                # boolean value is true if the user has entered correct password else false
                correct_password = check_password_hash(db_data.password_hash, user_data['password'])

                if correct_password:
                    # if user authentication is successfull, we store the user information
                    # in a session for futher use

                    # storing the username in a flask-session for later use
                    session['Username'] = username

                    # log message
                    print(f"__LOG__ Added a new session (with client side cookies) for User : {username}")
                    print(f"__LOG__ [SIGN IN] {username} ")

                    return redirect(url_for('user.user_page', username=username))
                else:
                    flash(f"INCORRECT PASSWORD!! Try again.", "ERROR")
                    return redirect(url_for('auth.signin'))
                    
        else:
            flash(f'Login Failed!! Try Again.', "ERROR")
            return redirect(url_for('auth.signin', form=form))
    



