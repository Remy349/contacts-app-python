from flaskr.main import bp
from flask import current_app, render_template, request, url_for
from flask_login import current_user, login_required

from flaskr.models import Contact


@bp.route("/")
@login_required
def index():
    page = request.args.get("page", 1, type=int)
    contacts = Contact.query.filter_by(user_id=current_user.id).paginate(
        page, current_app.config["CONTACTS_PER_PAGE"], False)

    next_url = url_for("main.index", page=contacts.next_num) \
        if contacts.has_next else None
    prev_url = url_for("main.index", page=contacts.prev_num) \
        if contacts.has_prev else None

    return render_template("index.html", contacts=contacts.items,
                           next_url=next_url, prev_url=prev_url)
