from app import app, db
from app.models import Exercise

def initialize_database():
    # Create app context
    with app.app_context():
        # Create and add exercises to the database
        exercise1 = Exercise(name='Push-up', description='Description of push-up exercise.', instructions='Instructions for performing push-up.', target_muscles='Chest, Shoulders, Triceps')
        exercise2 = Exercise(name='Squat', description='Description of squat exercise.', instructions='Instructions for performing squat.', target_muscles='Quadriceps, Hamstrings, Glutes')

        db.session.add(exercise1)
        db.session.add(exercise2)
        db.session.commit()

if __name__ == "__main__":
    initialize_database()
