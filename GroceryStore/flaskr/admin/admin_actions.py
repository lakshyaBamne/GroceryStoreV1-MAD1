#routes to take care of actions like delete and edit on the admin page

from flask import (
    session,
    flash,
    url_for,
    redirect
)

from flaskr.admin import bp

from flaskr.extensions import db

from flaskr.models import (
    Category
)

@bp.route("/admin/actions/delete/category/<int:id>")
def action_delete_category(id):
    """
        Endpoint to delete a category from the database when admin clicks a button
    """
    # delete the category from the database with given id
    to_delete = Category.query.get(id)

    db.session.delete(to_delete)
    db.session.commit()

    flash(f"__LOG__ [DELETE] successfully deleted category : {to_delete.id} -> {to_delete.name}", "SUCCESS")
    print(f"__LOG__ [DELETE] successfully deleted a category")
    return redirect(url_for("admin.admin", username=session["Username"]))

