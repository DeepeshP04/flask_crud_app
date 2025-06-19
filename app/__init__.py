from flask import Flask
from flask_pymongo import PyMongo
from .api.users import user_bp
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")

def create_app():
    DB_URL = os.getenv("MONGODB_URL")
    
    # Create flask app
    app = Flask(__name__)
    app.config["Mongo_URI"] = f"mongo://localhost:27017/{DB_URL}"
    mongo = PyMongo(app)
    
    # Register blueprints
    app.register_blueprint(user_bp)
    
    return app