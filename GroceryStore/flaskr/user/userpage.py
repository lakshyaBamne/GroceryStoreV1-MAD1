from flask import render_template

from flaskr.user import bp

@bp.route('/user/<username>', methods=['GET', 'POST'])
def user_page(username):
    return render_template('user/userpage.html', username=username)