from flask import (
    session,
    request,
    render_template,
    url_for,
    flash,
    redirect,
    jsonify
)

from flaskr.admin import bp

from flaskr.forms.admin_data_forms import (
    LocationForm,
    SellerForm,
    Unit,
    CategoryForm,
    ProductForm
)

from flaskr.models import Category

# importing utility functions
from flaskr.admin.utility.Utility import (
    get_categories
)


@bp.route("/admin/<username>", methods=["GET", "POST"])
def admin(username):
    """
        Admin page handler
    """

    # using our function to get the data from the database in json format
    # we can store all the data in a single dictionary which is
    # then passed to the template
    data = {}
    
    data[f"category"] = get_categories()

    # we need to render all the forms that appear in the modals here
    # and pass it to the templates using a dictionary object which 
    # can then be used inside the jinja templates
    location_form = LocationForm()
    seller_form = SellerForm()
    unit_form = Unit()
    category_form = CategoryForm()
    product_form = ProductForm()

    form ={
        "location" : location_form,
        "seller" : seller_form,
        "unit" : unit_form,
        "category" : category_form,
        "product" : product_form
    }

    # we want the database information in json form 
    # so we design an API for the database using a new blueprint

    if request.method == "GET":
        if 'Username' in session:
            if session['Username'] == username:
                return render_template('admin/admin_index.html', username=username, form=form, data=data)
            else:
                print(f"__LOG__ [POSSIBLE BREACH] someone tried to access account of {username}")
                return "<h1>Nice try hacker!! your tricks not working on this website</h1>"
        else:
            # replace this string with an error handler later
            print(f"__LOG__ [POSSIBLE BREACH] someone tried to access account of {username}")
            return "<h1>Nice try hacker!! your tricks not working on this website</h1>"
