from flask import (
    render_template, 
    session,
    redirect, 
    url_for
)

from flaskr.main import bp

from flaskr.utility.Utility import (
    get_categories
)

@bp.route("/", methods=["GET"])
def index():
    """
        view function to serve the home page for the website
    """
    data = {}

    data[f"category"] = get_categories()

    return render_template("main/index.html", data=data)