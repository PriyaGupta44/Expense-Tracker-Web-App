from datetime import date

from flask_wtf import FlaskForm

from wtforms import (
    DateField,
    DecimalField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField
)

from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange
)


class ExpenseForm(FlaskForm):

    title = StringField(
        "Title",
        validators=[
            DataRequired(
                message="Expense title is required."
            ),
            Length(
                min=2,
                max=150,
                message="Title must be between 2 and 150 characters."
            )
        ]
    )

    description = TextAreaField(
        "Description",
        validators=[
            Length(
                max=500,
                message="Description cannot exceed 500 characters."
            )
        ]
    )

    amount = DecimalField(
        "Amount",
        validators=[
            DataRequired(
                message="Amount is required."
            ),
            NumberRange(
                min=0.01,
                message="Amount must be greater than 0."
            )
        ],
        places=2
    )

    category = SelectField(
        "Category",
        choices=[
            ("food", "Food"),
            ("transport", "Transport"),
            ("shopping", "Shopping"),
            ("bills", "Bills & Utilities"),
            ("entertainment", "Entertainment"),
            ("health", "Health"),
            ("education", "Education"),
            ("other", "Other")
        ],
        validators=[
            DataRequired(
                message="Please select a category."
            )
        ]
    )

    expense_date = DateField(
        "Expense Date",
        validators=[
            DataRequired(
                message="Expense date is required."
            )
        ],
        default=date.today
    )

    submit = SubmitField("Add Expense")