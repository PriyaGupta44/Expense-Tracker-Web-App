from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from sqlalchemy.exc import SQLAlchemyError

from app.expenses import expenses
from app.expenses.forms import ExpenseForm
from app.extensions import db
from app.models import Expense


@expenses.route("/add", methods=["GET", "POST"])
@login_required
def add_expense():

    form = ExpenseForm()

    if form.validate_on_submit():

        expense = Expense(
            title=form.title.data.strip(),
            description=(
                form.description.data.strip()
                if form.description.data
                else None
            ),
            amount=form.amount.data,
            category=form.category.data,
            expense_date=form.expense_date.data,
            user_id=current_user.id
        )

        try:
            db.session.add(expense)
            db.session.commit()

        except SQLAlchemyError:

            db.session.rollback()

            flash(
                "Unable to save your expense. Please try again.",
                "danger"
            )

            return render_template(
                "expenses/add.html",
                form=form
            )

        flash(
            "Expense added successfully.",
            "success"
        )

        return redirect(
            url_for("expenses.list_expenses")
        )

    return render_template(
        "expenses/add.html",
        form=form
    )


@expenses.route("/")
@login_required
def list_expenses():

    expenses_list = (
        Expense.query
        .filter_by(user_id=current_user.id)
        .order_by(
            Expense.expense_date.desc(),
            Expense.created_at.desc()
        )
        .all()
    )

    return render_template(
        "expenses/list.html",
        expenses=expenses_list
    )