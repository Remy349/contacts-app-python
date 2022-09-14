from flask import Blueprint

bp = Blueprint("contact", __name__)

from flaskr.contact import routes
