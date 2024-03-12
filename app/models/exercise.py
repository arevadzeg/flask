from app import db



class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    target_muscles = db.Column(db.String(100), nullable=False)
    
    
    def __repr__(self):
        return f"WorkoutPlan(id={self.id}, name={self.name}, instructions={self.instructions}, description={self.description}, target_muscles={self.target_muscles})"