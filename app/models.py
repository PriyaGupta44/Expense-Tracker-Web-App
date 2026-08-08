from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from app.extensions import db

from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    created_at = db.Column(
        db.DateTime, nullable = False,
        default=datetime.utcnow
    )

    expenses = db.relationship(
        "Expense",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
            return f"<User {self.username}>"


class Expense(db.Model):
    __tablename__ = "expenses"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    amount = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=False
    )

    expense_date = db.Column(
        db.Date,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        nullable=False,
        index=True
    )

    def __repr__(self):
        return (
            f"<Expense {self.title} "
            f"- {self.amount}>"
        )