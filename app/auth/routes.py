from flask import flash, redirect, render_template, url_for
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

from app.auth import auth
from app.auth.forms import RegistrationForm
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
