from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import models to ensure tables are created
from app.models import User

# Create database tables
with app.app_context():
    db.create_all()

# Initialize Flask-JWT-Extended
jwt = JWTManager(app)



# Import routes at the end to avoid circular imports
from app import routes