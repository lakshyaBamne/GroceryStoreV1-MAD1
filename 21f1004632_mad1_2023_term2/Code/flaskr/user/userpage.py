from flask import (
    session,
    render_template
)

from flaskr.user import bp

from flaskr.utility.User import (
    get_user_data
)

from flaskr.utility.Admin import(
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
    
@bp.route('/user/home/<username>', methods=['GET','POST'])
def user_home(username):
    data = {}
    data[f"category"] = get_categories()
    data[f"user_data"] = get_user_data(username)

    if 'Username' in session:
        if session['Username'] == username:
            return render_template('user/userhome.html', username=username, data=data)
        else:
            print(f"__LOG__ [POSSIBLE BREACH] someone tried to access account of {username}")
            return "<h1>Nice try hacker!! your tricks not working on this website</h1>"
    else:
        # replace this string with an error handler later
        print(f"__LOG__ [POSSIBLE BREACH] someone tried to access account of {username}")
        return "<h1>Nice try hacker!! your tricks not working on this website</h1>"


@bp.route('/user/cart/<username>', methods=["GET", "POST"])
def user_cart(username):
    """
        view to take a user to their cart and show all the items for checkout
        also shows the items which are saved for later which can be moved to the cart later
    """
    if 'Username' in session:
        if session['Username'] == username:
            return render_template('user/usercart.html', username=username)
        else:
            print(f"__LOG__ [POSSIBLE BREACH] someone tried to access account of {username}")
            return "<h1>Nice try hacker!! your tricks not working on this website</h1>"
    else:
        # replace this string with an error handler later
        print(f"__LOG__ [POSSIBLE BREACH] someone tried to access account of {username}")
        return "<h1>Nice try hacker!! your tricks not working on this website</h1>"

