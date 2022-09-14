from flaskr.contact import bp
from flaskr import db
from flaskr.contact.forms import NewContact
from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from flaskr.models import Contact


@bp.route("/new", methods=["GET", "POST"])
@login_required
def new():
    form = NewContact()

    if form.validate_on_submit():
        contact = Contact(contact_name=form.contact_name.data,
                          contact_phonenumber=form.contact_phonenumber.data,
                          author=current_user)
        db.session.add(contact)
        db.session.commit()

        flash("Contact successfully saved!")

        return redirect(url_for("main.index"))

    return render_template("contact/new.html", title="New", form=form)
