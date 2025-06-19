from flask import Blueprint, jsonify, request
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
    
@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data["name"]
    email = data["email"]
    password = data["password"]
    
    if not name or not email or not password:
        return jsonify({"error": "Name, email and password are required."}), 400
    
    user = User(name=name, email=email, password=password)
    user.save()
    
    return jsonify({"message": "User created successfully.", "user": user}), 201