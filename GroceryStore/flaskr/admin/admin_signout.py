from flask import (
    session,
    request,
    url_for,
    redirect,
    render_templater,
    flash
)

from flaskr.admin import bp

@bp.route('', methods=["GET", "POST"])
def admin_signout():
    """
        View function to log out a user

        -> also destroy cookies of the user
    """
    if request.method == "GET":
        if 'Username' in session:
            # log message
            print(f"__LOG__ Destroyed the session for Admin : {session['Username']}")
            print(f"__LOG__ [SIGN OUT] {session['Username']} ")

            session.pop('Username')
        
    return redirect(url_for('app.index'))

