from flask import Blueprint

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")

@user_bp.route("/")
def get_users():
    return {"users": []}