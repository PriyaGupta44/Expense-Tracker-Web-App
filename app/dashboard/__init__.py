from flask import Blueprint


dashboard = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard",
    template_folder="templates"
)


from app.dashboard import routes