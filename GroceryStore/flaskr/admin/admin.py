from flask import (
    session,
    request,
    render_template,
    url_for,
    flash,
    redirect
)

from flaskr.admin import bp

from flaskr.forms.admin_data_forms import LocationForm

@bp.route("/admin/<username>", methods=["GET", "POST"])
def admin(username):
    """
        Admin page handler
    """

    # we need to render all the forms that appear in the modals here
    # and pass it to the templates
    location_form = LocationForm()

    form ={
        "location" : location_form
    }

    if request.method == "GET":
        if 'Username' in session:
            if session['Username'] == username:
                return render_template('admin/admin_index.html', username=username, form=form)
            else:
                print(f"__LOG__ [POSSIBLE BREACH] someone tried to access account of {username}")
                return "<h1>Nice try hacker!! your tricks not working on this website</h1>"
        else:
            # replace this string with an error handler later
            print(f"__LOG__ [POSSIBLE BREACH] someone tried to access account of {username}")
            return "<h1>Nice try hacker!! your tricks not working on this website</h1>"