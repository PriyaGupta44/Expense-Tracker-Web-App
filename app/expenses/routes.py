from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from sqlalchemy.exc import SQLAlchemyError

from app.expenses import expenses
from app.expenses.forms import ExpenseForm
from app.extensions import db
from app.models import Expense

from app.expenses.forms import(DeleteExpenseForm, ExpenseForm)


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

    delete_form = DeleteExpenseForm()

    return render_template(
        "expenses/list.html",
        expenses=expenses_list, 
        delete_form=delete_form
    )

@expenses.route("/<int:expense_id>/edit", methods=["GET", "POST"])
@login_required
def edit_expense(expense_id):

    expense = Expense.query.filter_by(
        id = expense_id,
        user_is = current_user.id
    ).first_or_404()

    form = ExpenseForm(obj=expense)

    if form.validate_on_submit():
        expense.title = form.title.data.strip()

        expense.description = (
            form.description.data.strip()
            if form.description.data
            else None
        )

        expense.amount = form.amount.data
        expense.category = form.category.data
        expense.expense_date = form.expense_date.data

        try:

            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()

            flash("Unable to update your expense." "Please try again", "danger")

            return render_template("expenses/edit.html", form=form, expense=expense)

        flash("Expence updated successfully","success")
        return redirect(url_for("expenses.list_expences"))

    return render_template(
        "expenses/edit.html", form=form, expense=expense
    )

@expenses.route("/<int:expense_id>/delete", methods=["POST"])
@login_required
def delete_expense(expense_id):

    expense = Expense.query.filter_by(
        id=expense_id,
        user_id=current_user.id
    ).first_or_404()

    form = DeleteExpenseForm()

    if not form.validate_on_submit():

        flash(
            "Invalid delete request.",
            "danger"
        )

        return redirect(
            url_for("expenses.list_expenses")
        )

    try:

        db.session.delete(expense)
        db.session.commit()

    except SQLAlchemyError:

        db.session.rollback()

        flash(
            "Unable to delete your expense. "
            "Please try again.",
            "danger"
        )

        return redirect(
            url_for("expenses.list_expenses")
        )

    flash(
        "Expense deleted successfully.",
        "success"
    )

    return redirect(
        url_for("expenses.list_expenses")
    )