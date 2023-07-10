from flask import (
    session,
    request,
    render_template,
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
        if 'Username' in session:
            if session['Username'] == username:
                return render_template('user/userpage.html', username=username)
            else:
                print(f"__LOG__ [POSSIBLE BREACH] someone tried to access account of {username}")
                return "<h1>Nice try hacker!! your tricks not working on this website</h1>"
        else:
            # replace this string with an error handler later
            print(f"__LOG__ [POSSIBLE BREACH] someone tried to access account of {username}")
            return "<h1>Nice try hacker!! your tricks not working on this website</h1>"
    elif request.method == "POST":
        pass