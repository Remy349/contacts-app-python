from flaskr.auth import bp
from flaskr.auth.forms import SignInForm
from flask import render_template


@bp.route("/sign-in", methods=["GET", "POST"])
def signin():
    return render_template("auth/signin.html", title="Sign In")
