from flaskr.contact import bp
from flaskr import db
from flaskr.contact.forms import ContactForm
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from flaskr.models import Contact


@bp.route("/new", methods=["GET", "POST"])
@login_required
def new():
    form = ContactForm()

    if form.validate_on_submit():
        contact = Contact(contact_name=form.contact_name.data,
                          contact_phonenumber=form.contact_phonenumber.data,
                          author=current_user)
        db.session.add(contact)
        db.session.commit()

        flash("Contact successfully saved!")

        return redirect(url_for("main.index"))

    return render_template("contact/new.html", title="New", form=form,
                           text="New")


@bp.route("/edit/<id>", methods=["GET", "POST"])
@login_required
def edit(id):
    form = ContactForm()

    edit_contact = Contact.query.filter_by(id=id).first()

    if form.validate_on_submit():
        edit_contact.contact_name = form.contact_name.data
        edit_contact.contact_phonenumber = form.contact_phonenumber.data

        db.session.commit()

        flash("Contact successfully edited!")

        return redirect(url_for("main.index"))
    elif request.method == "GET":
        form.contact_name.data = edit_contact.contact_name
        form.contact_phonenumber.data = edit_contact.contact_phonenumber

    return render_template("contact/new.html", title="Edit", form=form,
                           text="Edit")


@bp.route("/delete/<id>", methods=["GET"])
@login_required
def delete(id):
    delete_contact = Contact.query.filter_by(id=id).first()
    db.session.delete(delete_contact)
    db.session.commit()

    flash("Contact successfully deleted!")

    return redirect(url_for("main.index"))
