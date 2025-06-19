from flask import Blueprint, jsonify
from ..models import User
from ..extensions import mongo
from bson import ObjectId

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")

@user_bp.route("/")
def get_users():
    users = mongo.db.users.find()
    return jsonify({"users": users}), 200

@user_bp.route("/<user_id>")
def get_user_by_id(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
        return jsonify({"user": user}), 200
    else:
        return jsonify({"error": "User not found."}), 404