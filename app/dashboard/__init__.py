from flask import Blueprint
from app.dashboard import routes

dashboard = Blueprint(
    "dashboard", __name__, 
    url_prefix="/dashboard",
    template_folder="templates"
)

