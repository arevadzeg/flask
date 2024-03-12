

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Initialize SQLAlchemy
db = SQLAlchemy(app)


# Create database tables
with app.app_context():
    db.create_all()

# Initialize Flask-JWT-Extended
jwt = JWTManager(app)

# Serve Swagger UI
SWAGGER_URL = '/api/docs'  # URL for accessing Swagger UI
API_URL = '/static/swagger.json'   # URL for accessing Swagger JSON file


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Import routes at the end to avoid circular imports
from app import routes
