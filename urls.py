from flask import Blueprint
from view import index, h

news_bp = Blueprint('news',__name__)

@news_bp.route("/")
def _(): return index()

@news_bp.route("/h")
def __(): return h()