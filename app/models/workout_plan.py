from app import db


class WorkoutPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    frequency = db.Column(db.String(50), nullable=False)
    goals = db.Column(db.Text, nullable=False)
    session_duration = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"WorkoutPlan(id={self.id}, user_id={self.user_id})"


