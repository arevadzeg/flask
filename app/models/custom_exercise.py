from app import db

class CustomExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    repetitions = db.Column(db.Integer, nullable=True)
    sets = db.Column(db.Integer, nullable=True)
    duration = db.Column(db.Integer, nullable=True)  # In minutes
    distance = db.Column(db.Float, nullable=True)   # In kilometers, for exercises like running

    def __repr__(self):
        return f"CustomExercise(id={self.id}, user_id={self.user_id}, exercise_id={self.exercise_id})"
