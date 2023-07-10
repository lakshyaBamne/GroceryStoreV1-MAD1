from flask import (
    request,
    session,
    flash,
    render_template,
    redirect,
    url_for
)

from flaskr.auth import bp

@bp.route("/signout", methods=["GET", "POST"])
def signout():
    """
        View function to sign out a user from our website

        -> destroy the stored cookies
    """
    if request.method == "GET":
        if 'Username' in session:
            # log message
            print(f"__LOG__ Destroyed the session for User : {session['Username']}")
            print(f"__LOG__ [SIGN OUT] {session['Username']} ")

            session.pop('Username')
        
    return redirect(url_for('app.index'))
            

