from flaskr import db
from werkzeug.urls import url_parse
from flaskr.auth import bp
from flaskr.auth.forms import SignInForm, SignUpForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user

from flaskr.models import User


@bp.route("/sign-in", methods=["GET", "POST"])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = SignInForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password!")
            return redirect(url_for("auth.signin"))

        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get("next")

        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("main.index")

        return redirect(next_page)

    return render_template("auth/signin.html", form=form)


@bp.route("/sign-up", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = SignUpForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.signin"))

    return render_template("auth/signup.html", title="Sign Up",
                           form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))
