from flask import Blueprint, jsonify
from ..models import User
from ..extensions import mongo

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")

@user_bp.route("/")
def get_users():
    users = mongo.db.users.find()
    return jsonify({"users": users})