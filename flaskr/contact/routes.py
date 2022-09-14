from flaskr.contact import bp
from flaskr import db
from flaskr.contact.forms import NewContact
from flask import redirect, render_template, url_for
from flask_login import login_required

from flaskr.models import Contact


@bp.route("/new", methods=["GET", "POST"])
@login_required
def new():
    form = NewContact()

    if form.validate_on_submit():
        print(form.contact_name.data, form.contact_phonenumber.data)

        return redirect(url_for("main.index"))

    return render_template("contact/new.html", title="New", form=form)
