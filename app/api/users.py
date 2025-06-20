from flask import Blueprint, jsonify, request
from ..models import User
from ..extensions import mongo
from bson import ObjectId
from ..utils import hash_password

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")

# Get all users
@user_bp.route("/")
def get_users():
    users = mongo.db.users.find()
    user_list = []
    
    for user in users:
        user["_id"] = str(user["_id"])
        user_list.append(user)
        
    if user_list:
        return jsonify({"users": user_list}), 200
    else:
        return jsonify({"error": "No user found."}), 404

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
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    
    if not name or not email or not password:
        return jsonify({"error": "Name, email and password are required."}), 400
    
    # Hash the password
    hashed_pass = hash_password(password)
    
    # Create and save the user
    user = User(name=name, email=email, password=hashed_pass)
    user.save()
    
    return jsonify({"message": "User created successfully."}), 201

# Update the user data
@user_bp.route("/<id>", methods=["PUT"])
def update_user_data(id):
    data = request.get_json()
    update_fields = {}
    
    if "name" in data:
        update_fields["name"] = data["name"]
    if "email" in data:
        update_fields["email"] = data["email"]
    if "password" in data:
        update_fields["password"] = hash_password(data["password"])
        
    if not update_fields:
        return jsonify({"error": "No fields provided to update."}), 400
    
    result = mongo.db.users.update_one(
        {"_id": ObjectId(id)},
        {"$set": update_fields}
    )
    
    if result.matched_count > 0:
        return jsonify({"message": "User details updated."}), 200
    else: 
        return jsonify({"error": "User not found."}), 404
 
# Delete a user by id   
@user_bp.route("/<id>", methods=["DELETE"])
def delete_user(id):
    user = mongo.db.users.delete_one({"_id": ObjectId(id)})
    if user.deleted_count == 1:
        return jsonify({"message": "User deleted successfully."}), 200
    else:
        return jsonify({"error": "User not found."}), 404