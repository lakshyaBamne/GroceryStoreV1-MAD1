from flask import (
    render_template,
    request,
    url_for,
    flash,
    redirect
)

from werkzeug.security import check_password_hash

from flaskr.admin import bp
from flaskr.forms import AdminSigninForm
from flaskr.models import Admin

@bp.route('/admin-signin', methods=["GET", "POST"])
def admin_signin():
    """
        View function to handle all the admin functions
    """
    form = AdminSigninForm()
    
    if request.method == 'GET':
        return render_template("admin/admin_signin.html", form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            # if user submits the form with all validators, we need to authenticate the user
            user_data = request.form

            username = user_data['username']

            # we need to get the stored hash in the database to validate the password
            db_data = Admin.query.filter_by(user_name=username).first()

            if db_data is None:
                # an admin with the given username does not exist
                flash(f"A user with the given username DOES NOT EXIST!! Try again.", "ERROR")
                return render_template("auth/signin.html", form=form)
            else:
                # an Admin with the given username EXISTS in the database

                # boolean value is true if the user has entered correct password else false
                correct_password = check_password_hash(db_data.password_hash, user_data['password'])

                if correct_password:
                    return redirect(url_for('admin.admin'))
                else:
                    flash(f"INCORRECT PASSWORD!! Try again.", "ERROR")
                    return redirect(url_for('admin.admin_signin'))
                    
        else:
            flash(f'Login Failed!! Try Again.', "ERROR")
            return redirect(url_for('admin.admin_signin'))