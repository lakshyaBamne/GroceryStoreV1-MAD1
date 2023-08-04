from flask import (
    session,
    render_template
)

from flaskr.user import bp

from flaskr.utility.Utility import (
    get_categories
)

@bp.route('/user/<username>', methods=['GET', 'POST'])
def user_page(username):
    data = {}

    data[f"category"] = get_categories()

    if 'Username' in session:
        if session['Username'] == username:
            return render_template('user/userpage.html', username=username, data=data)
        else:
            print(f"__LOG__ [POSSIBLE BREACH] someone tried to access account of {username}")
            return "<h1>Nice try hacker!! your tricks not working on this website</h1>"
    else:
        # replace this string with an error handler later
        print(f"__LOG__ [POSSIBLE BREACH] someone tried to access account of {username}")
        return "<h1>Nice try hacker!! your tricks not working on this website</h1>"