# Flask CRUD App
A simple and modular **Flask** application that performs **CRUD operations** on a **MongoDB** database using **Flask-PyMongo**. Passwords are securely hashed using `bcrypt`.

## Setup instructions

1. **Clone the repo**  
git clone https://github.com/DeepeshP04/flask_crud_app.git
cd flask_crud_app

2. **Create a .env file in the root directory:**   
DB_NAME=database_name  
FLASK_SECRET_KEY=your_secret_key  

3. **Create and activate a virtual environment**   
python -m venv venv
venv/Scripts/activate

4. **Install dependencies**  
pip install -r requirements.txt

5. **Start MongoDB locally**  
Make sure mongodb is running on localhost:27017

6. **Run the app**   
python run.py

## Dependencies
- Flask
- Flask-Pymongo
- python-dotenv
- bcrypt