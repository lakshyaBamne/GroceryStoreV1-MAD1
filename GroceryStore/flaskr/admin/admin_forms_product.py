from flask import (
    request,
    session,
    redirect,
    url_for,
    flash,
    render_template
)

from datetime import datetime, timezone

from flaskr.admin import bp

from werkzeug.security import check_password_hash

from flaskr.models import (
    Admin,
    Product,
    Category,
    Seller,
    MeasurementUnit
)
from flaskr.extensions import db
from flaskr.forms.admin_data_forms import (
    CategoryForm,
    ProductForm
)

# we make different routed for the different forms in the Admin Dashboard

@bp.route("/admin/forms/category", methods=["GET", "POST"])
def admin_form_category():
    """
        Admin dashboard handler for Form-Adding a new category
    """

    if request.method == "POST":
        print(f"__LOG__ Admin {session['Username']} submitted a POST request to /admin/forms/category ...")

        form = CategoryForm(request.form) 

        if form.validate():
            form_data = request.form

            category_name = (lambda name: name.upper())(form_data['name'])
            category_description = form_data['description']
            password = form_data['password']

            # check if the password is correct or not
            password_is_correct = (lambda password: check_password_hash( Admin.query.filter_by(user_name=session['Username']).first().password_hash , password))(password)

            if password_is_correct:
                # proceed to check correctness of data and then add to database
                category_exists = (lambda c_name: True if Category.query.filter_by(name=c_name).first() else False)(category_name)

                if category_exists:
                    flash(f"__LOG__ Category already exists! No changes were made to the Database!", "WARNING")
                    return redirect(url_for("admin.admin", username=session['Username']))
                else:
                    # seller does not exist so we can add one
                    new_unit = Category(name=category_name, description=category_description)

                    db.session.add(new_unit)
                    db.session.commit()

                    flash(f"__LOG__ Successfully added a new category : {category_name}", "SUCCESS")
                    return redirect(url_for("admin.admin", username=session['Username']))

            else:
                flash("__ERROR__ : Admin Password wrong!! try again", "ERROR")
                return redirect(url_for("admin.admin", username=session['Username']))

        else:
            if form.errors:
                for error in form.errors:
                    flash(f"__ERROR__ : {error} : {form.errors[error][0]} | ", "ERROR")
            return redirect(url_for("admin.admin", username=session['Username']))


@bp.route("/admin/forms/product", methods=["GET", "POST"])
def admin_form_product():
    """
        Admin dashboard handler for Form-Adding a new product
    """

    if request.method == "POST":
        print(f"__LOG__ Admin {session['Username']} submitted a POST request to /admin/forms/product ...")

        form = ProductForm(request.form) 

        if form.validate():
            form_data = request.form

            product_name = (lambda name: name.upper())(form_data['name'])
            product_description = form_data['description']
            
            # we need to match the ID of this entered category from database then do addition
            product_category = (lambda name: name.upper())(form_data['category'])

            product_quantity = form_data['quantity']

            # we need to match the ID of this entered unit from database then do addition
            product_unit = (lambda name: name.upper())(form_data['unit'])
            product_price = form_data['price_per_quantity']

            # we need to match the ID of this entered seller from database then do addition
            seller_name = (lambda name: name.upper())(form_data['seller'])

            # we need to convert then to required form then add to database
            # product_date_added = form_data['date_added'] if form_data['date_added'] else datetime.now(timezone.utc)
            product_expiration_date =  datetime.strptime(form_data['expiration_date'], '%Y-%m-%d') 

            password = form_data['password']

            # check if the password is correct or not
            password_is_correct = (lambda password: check_password_hash( Admin.query.filter_by(user_name=session['Username']).first().password_hash , password))(password)

            if password_is_correct:
                # proceed to check correctness of data and then add to database
                product_exists = (lambda c_name: True if Product.query.filter_by(name=c_name).first() else False)(product_name)

                if product_exists:
                    flash(f"__LOG__ Product already exists! No changes were made to the Database!", "WARNING")
                    return redirect(url_for("admin.admin", username=session['Username']))
                else:
                    # product does not exist so we can add one
                    category_id = Category.query.filter_by(name=product_category).first().id
                    seller_id = Seller.query.filter_by(name=seller_name).first().id
                    unit_id = MeasurementUnit.query.filter_by(name=product_unit).first().id
                    
                    new_product = Product(name=product_name, description=product_description , category=category_id, quantity=product_quantity, unit=unit_id, price_per_quantity=product_price, seller=seller_id,  expiration_date=product_expiration_date)

                    db.session.add(new_product)
                    db.session.commit()

                    flash(f"__LOG__ Successfully added a new product : {product_name}", "SUCCESS")
                    return redirect(url_for("admin.admin", username=session['Username']))

            else:
                flash("__ERROR__ : Admin Password wrong!! try again", "ERROR")
                return redirect(url_for("admin.admin", username=session['Username']))

        else:
            if form.errors:
                for error in form.errors:
                    flash(f"__ERROR__ : {error} : {form.errors[error][0]} | ", "ERROR")
            return redirect(url_for("admin.admin", username=session['Username']))
