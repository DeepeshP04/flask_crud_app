from flask import Flask
from .extensions import mongo
from .api.users import user_bp
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")

def create_app():
    DB_NAME = os.getenv("DB_NAME")
    
    # Create flask app
    app = Flask(__name__)
    app.config["MONGO_URI"] = f"mongodb://localhost:27017/{DB_NAME}"
    mongo.init_app(app)
    
    # Register blueprints
    app.register_blueprint(user_bp)
    
    return app