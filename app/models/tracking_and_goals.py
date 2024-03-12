from app import db

class TrackingAndGoals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    fitness_goals = db.Column(db.Text)
    achievements = db.Column(db.Text)

    def __repr__(self):
        return f"TrackingAndGoals(id={self.id}, user_id={self.user_id}, date={self.date}, weight={self.weight})"
