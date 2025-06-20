from flask import Flask
from .extensions import mongo
from .api.users import user_bp
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")
DB_NAME = os.getenv("DB_NAME")
SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

def create_app():
    
    # Create flask app
    app = Flask(__name__)
    app.config["MONGO_URI"] = f"mongodb://localhost:27017/{DB_NAME}"
    mongo.init_app(app)
    app.secret_key = SECRET_KEY
    
    # Register blueprints
    app.register_blueprint(user_bp)
    
    return app