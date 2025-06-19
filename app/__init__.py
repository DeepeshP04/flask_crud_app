from flask import Flask
from api.users import user_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(user_bp)
    
    app.run(debug=True)

if __name__== "__main__":
    create_app()