from flask import (
    request,
    session,
    url_for,
    redirect,
    render_template,
    flash
)

from werkzeug.security import check_password_hash

from flaskr.admin import bp

from flaskr.extensions import db

from flaskr.forms.admin_data_forms import (
    LocationForm
)

from flaskr.models import (
    Admin,
    City,
    State,
    Country,
    Location
)

@bp.route("/admin/forms/location", methods=["GET", "POST"])
def admin_forms_location():
    """
        Admin dashboard handler for Form-Adding a new location for
        the store to operate in.

        -> This view function only handles the POST request on the form
        -> the form is rendered in a modal in the admin/admin_index.html file
    """
    if request.method == "POST":
        # instantiate the form object with the one in the form
        form = LocationForm(request.form)

        if form.validate():
            # now we need to check if the Location already exists, if no then add to database
            # else flash another warning message saying that entered location already exists
            form_data = request.form

            # details coming from the form submitted by the admin
            city_name = (lambda name: name.upper())(form_data['city'])
            state_name = (lambda name: name.upper())(form_data['state'])
            country_name = (lambda name: name.upper())(form_data['country'])
            password = form_data['password']

            # if the form is submitted with wrong ADMIN password, no changes are made
            # to the database
            password_is_correct = (lambda password: check_password_hash( Admin.query.filter_by(user_name=session['Username']).first().password_hash , password))(password)

            if password_is_correct:
                country_exits = (lambda country: True if Country.query.filter_by(name=country).first() else False)(country_name)
                state_exists = (lambda state: True if State.query.filter_by(name=state).first() else False)(state_name)
                city_exists = (lambda city: True if City.query.filter_by(name=city).first() else False)(city_name)

                print(country_exits, " ", state_exists, " ", city_exists)

                # proceed to add elements to the database

                # this dictionary stores the ids of city, state, country from the database
                location_ids = {}

                # first check if given country exits
                if not country_exits:
                    # add country to the table
                    new_country = Country(name=country_name)

                    db.session.add(new_country)
                    db.session.commit()

                    flash(f"__SUCCESS__ Added new country : {country_name} to Database", "SUCCESS")
                else:
                    # add id of existing country to the dictionary object
                    pass

                # now check if the state exists

                if not state_exists:
                    # add state to the table
                    new_state = State(name=state_name)

                    db.session.add(new_state)
                    db.session.commit()

                    flash(f"__SUCCESS__ Added new state : {state_name} to Database", "SUCCESS")
                else:
                    # add id of existing state to the dictionary object
                    pass

                # now check if the city exists

                if not city_exists:
                    # add state to the table
                    new_city = City(name=city_name)

                    db.session.add(new_city)
                    db.session.commit()

                    flash(f"__SUCCESS__ Added new city : {city_name} to Database", "SUCCESS")
                else:
                    # add id of existing state to the dictionary object
                    pass

                location_ids["COUNTRY_ID"] = Country.query.filter_by(name=country_name).first().id
                location_ids["STATE_ID"] = State.query.filter_by(name=state_name).first().id
                location_ids["CITY_ID"] = City.query.filter_by(name=city_name).first().id
                
                print("__LOG__ Added a new Store Location : ",location_ids)

                # now make a new location using the ids of the city, state and country
                new_location = Location(city_id=location_ids["CITY_ID"], state_id=location_ids["STATE_ID"], country_id=location_ids["COUNTRY_ID"])

                db.session.add(new_location)
                db.session.commit()

                flash(f"__SUCCESS__ Added new Location to Database", "SUCCESS")
                return redirect(url_for("admin.admin", username=session['Username']))
            else:
                flash("__ERROR__ : Admin Password wrong!! try again", "ERROR")
                return redirect(url_for("admin.admin", username=session['Username']))

            # all data correctly entered
            flash("Location Form Sucessfully Submitted! ADDED NEW LOCATION", "SUCCESS")
            return redirect(url_for("admin.admin", username=session['Username']))
        else:
            if form.errors:
                for error in form.errors:
                    flash(f"__ERROR__ : {error} : {form.errors[error][0]} | ", "ERROR")
            return redirect(url_for("admin.admin", username=session['Username']))


            
