from flaskr.contact import bp
from flaskr import db
from flaskr.contact.forms import NewContact
from flask import render_template
from flask_login import login_required

from flaskr.models import Contact


@bp.route("/new", methods=["GET", "POST"])
@login_required
def new():
    form = NewContact()

    return render_template("contact/new.html", title="New", form=form)
