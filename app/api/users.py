from flask import Blueprint, jsonify, request
from ..models import User
from ..extensions import mongo
from bson import ObjectId

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")

# Get all users
@user_bp.route("/")
def get_users():
    users = mongo.db.users.find()
    return jsonify({"users": users}), 200

# Get a specific user by id
@user_bp.route("/<id>")
def get_user_by_id(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    if user:
        user["_id"] = str(user["_id"])
        return jsonify({"user": user}), 200
    else:
        return jsonify({"error": "User not found."}), 404
    
# Create a new user
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

# Update the user data
@user_bp.route("/id")
def update_user_data(id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    
    result = mongo.db.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"name": name, "email": email, "password": password}}
    )
    
    if result.matched_count() > 0:
        return jsonify({"message": "User details updated."}), 200
    else: 
        return jsonify({"error": "User not found."}), 404