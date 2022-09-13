from flaskr.main import bp
from flask import render_template
from flask_login import login_required


@bp.route("/")
@login_required
def index():
    contacts = [
        {"contactName": "Test1", "contactPhone": "0000 0000"},
        {"contactName": "Test2", "contactPhone": "0000 0000"},
        {"contactName": "Test3", "contactPhone": "0000 0000"},
        {"contactName": "Test4", "contactPhone": "0000 0000"}
    ]

    return render_template("index.html", contacts=contacts)
