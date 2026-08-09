from flask import Blueprint


expenses = Blueprint(
    "expenses",
    __name__,
    url_prefix="/expenses",
    template_folder="templates"
)


from app.expenses import routes