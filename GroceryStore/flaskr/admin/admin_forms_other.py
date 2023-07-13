from flask import (
    request,
    session,
    redirect,
    url_for,
    render_template,
    flash
)

from werkzeug.security import check_password_hash

from flaskr.models import(
    Admin, 
    Seller,
    MeasurementUnit
)
from flaskr.admin import bp
from flaskr.extensions import db
from flaskr.forms.admin_data_forms import (
    SellerForm,
    Unit
)

@bp.route("/admin/forms/unit", methods=["GET", "POST"])
def admin_form_unit():
    """
        Admin dashboard handler for Form-Adding a unit of measurement
    """

    if request.method == "POST":
        print(f"__LOG__ Admin {session['Username']} submitted a POST request to /admin/forms/unit ...")

        form = Unit(request.form) 

        if form.validate():
            form_data = request.form

            unit_name = (lambda name: name.upper())(form_data['name'])
            unit_shorthand = (lambda name: name.upper())(form_data['shorthand'])
            password = form_data['password']

            # check if the password is correct or not
            password_is_correct = (lambda password: check_password_hash( Admin.query.filter_by(user_name=session['Username']).first().password_hash , password))(password)

            if password_is_correct:
                # proceed to check correctness of data and then add to database
                unit_exists = (lambda u_name: True if MeasurementUnit.query.filter_by(name=u_name).first() else False)(unit_name)

                if unit_exists:
                    flash(f"__LOG__ Unit already exists! No changes were made to the Database!", "WARNING")
                    return redirect(url_for("admin.admin", username=session['Username']))
                else:
                    # seller does not exist so we can add one
                    new_unit = MeasurementUnit(name=unit_name, shorthand=unit_shorthand)

                    db.session.add(new_unit)
                    db.session.commit()

                    flash(f"__LOG__ Successfully added a new Seller/Brand : {unit_name}({unit_shorthand})", "SUCCESS")
                    return redirect(url_for("admin.admin", username=session['Username']))

            else:
                flash("__ERROR__ : Admin Password wrong!! try again", "ERROR")
                return redirect(url_for("admin.admin", username=session['Username']))

        else:
            if form.errors:
                for error in form.errors:
                    flash(f"__ERROR__ : {error} : {form.errors[error][0]} | ", "ERROR")
            return redirect(url_for("admin.admin", username=session['Username']))

@bp.route("/admin/forms/seller", methods=["GET", "POST"])
def admin_form_seller():
    """
        Admin dashboard handler for Form-Adding a seller to the web store
    """

    if request.method == "POST":
        print(f"__LOG__ Admin {session['Username']} submitted a POST request to /admin/forms/seller ...")

        form = SellerForm(request.form) 

        if form.validate():
            form_data = request.form

            seller_name = (lambda name: name.upper())(form_data['name'])
            seller_contact = form_data['contact']
            seller_email = form_data['email']
            password = form_data['password']

            # check if the password is correct or not
            password_is_correct = (lambda password: check_password_hash( Admin.query.filter_by(user_name=session['Username']).first().password_hash , password))(password)

            if password_is_correct:
                # proceed to check correctness of data and then add to database
                seller_exists = (lambda s_name: True if Seller.query.filter_by(name=s_name).first() else False)(seller_name)

                if seller_exists:
                    flash(f"__LOG__ Seller already exists! No changes were made to the Database!", "WARNING")
                    return redirect(url_for("admin.admin", username=session['Username']))
                else:
                    # seller does not exist so we can add one
                    new_seller = Seller(name=seller_name, seller_contact=seller_contact, seller_email=seller_email)

                    db.session.add(new_seller)
                    db.session.commit()

                    flash(f"__LOG__ Successfully added a new Seller/Brand : {seller_name}", "SUCCESS")
                    return redirect(url_for("admin.admin", username=session['Username']))

            else:
                flash("__ERROR__ : Admin Password wrong!! try again", "ERROR")
                return redirect(url_for("admin.admin", username=session['Username']))

        else:
            if form.errors:
                for error in form.errors:
                    flash(f"__ERROR__ : {error} : {form.errors[error][0]} | ", "ERROR")
            return redirect(url_for("admin.admin", username=session['Username']))