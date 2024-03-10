from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"



class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    target_muscles = db.Column(db.String(100), nullable=False)
    # Add more fields as needed


class WorkoutPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    frequency = db.Column(db.String(50), nullable=False)
    goals = db.Column(db.Text, nullable=False)
    session_duration = db.Column(db.Integer, nullable=False)
    # Add more fields as needed

    def __repr__(self):
        return f"WorkoutPlan(id={self.id}, user_id={self.user_id})"



class TrackingAndGoals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    fitness_goals = db.Column(db.Text)
    achievements = db.Column(db.Text)

    def __repr__(self):
        return f"TrackingAndGoals(id={self.id}, user_id={self.user_id}, date={self.date}, weight={self.weight})"
