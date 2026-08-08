from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user

from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

from app.auth import auth
from app.auth.forms import RegistrationForm, LoginForm
from app.extensions import db
from app.models import User

@auth.route("/register", method=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data.strip()
        email = form.email.data.strip().lower()

        existing_username = User.query.filter(
            func.lower(User.username) == username.lower()
        ).first()

        if existing_username:
            flash("That username is already taken.", "danger")
            return render_template("auth/register.html", form=form)

        existing_email = User.query.filter(
            func.lower(User.email) == email
        ).first()

        if existing_email:
            flash("An account with that email is already exists.", "danger")
            return render_template("auth/register.html", form=form)

        user = User(
            username=username,
            email=email
        )

        user.set_password(form.password.data)

        try:
            db.session.add(user)
            db.session.commit()

        except SQLAlchemyError:
            db.session.rollback()

            flash("Unable to create your account right now. Please try again.","danger")
            return render_template("auth/register.html", form=form)

        flash("Account Created Sucessfully. you cam now log in.", "success")
        return redirect(url_for("main.home"))

    return render_template(
        "auth/register.html",
        form=form
    )

@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data.strip().lower()

        user = User.query.filter(
            func.lower(User.email) == email
        ).first()

        if user is None or not user.check_password(
            form.password.data
        ):
            flash("Invalid email or password", "danger")
            return render_template("auth/login.html", form=form)

        login_user(user, remember=form.remember.data)
        flash(f"Welcome back, {user.username}!", "success")
        return redirect(url_for("main.home"))

    return render_template("auth/login.html",form=form)


@auth.route("/logout", mathod=["POST"])
def logout():
    logout_user()

    flash("You have been logged out sucessfully.", info)
    return redirect(url_for("main.home"))
    
