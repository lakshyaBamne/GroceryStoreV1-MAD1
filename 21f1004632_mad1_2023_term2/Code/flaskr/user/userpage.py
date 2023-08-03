from flask import render_template, session

from flaskr.user import bp

@bp.route('/user/<username>', methods=['GET', 'POST'])
def user_page(username):
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