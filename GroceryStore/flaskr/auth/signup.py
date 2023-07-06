from flask import (
    render_template,
    request,
    flash,
    redirect,
    url_for
)

from werkzeug.security import generate_password_hash

from flaskr.auth import bp
from flaskr.extensions import db
from flaskr.forms import SignupForm
from flaskr.models import User

@bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if request.method == 'GET':
        return render_template("auth/signup.html", form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            # user submits the correct data and hence can be registered
            new_user_data = request.form

            full_name = new_user_data['name']
            user_name = new_user_data['username']
            email = str(new_user_data['email'])
            contact = new_user_data['contact']
            password_hash = generate_password_hash(new_user_data['password_hash'])

            u = User(full_name=full_name, user_name=user_name, email=email,contact=contact, password_hash=password_hash)

            # now we can try and add the new used to the database
            try:
                db.session.add(u)
                db.session.commit()
                
                # after creating the user we can redirect them to their personalized home page
                print(f"[LOG] Added a new user successfully -> {u}")
                flash(f"Success! Added new user.", "SUCCESS")
                return redirect(url_for('auth.signin'))
            
            except:
                flash(f"Error creating user!! Try again.", "ERROR")
                return render_template("auth/signup.html", form=form)


        else:
            # user did not submit the correct data for all fields
            return render_template("auth/signup.html", form=form)