
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"
    
    def validate(self):
        errors = []
        if len(self.username) > 50:
            errors.append("Username must be 50 characters or less")
        if len(self.password) < 6:
            errors.append("Password must be at least 6 characters long")
        if errors:
            raise ValueError("Validation failed:", errors)
