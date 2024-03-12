from app import app, db
from app.models.exercise import Exercise

def initialize_database():
    with app.app_context():
        # Create and add exercises to the database
        exercise1 = Exercise(name='Push-up', description='Description of push-up exercise.', instructions='Instructions for performing push-up.', target_muscles='Chest, Shoulders, Triceps')
        db.session.add(exercise1)

        exercise2 = Exercise(name='Squat', description='Description of squat exercise.', instructions='Instructions for performing squat.', target_muscles='Quadriceps, Hamstrings, Glutes')
        db.session.add(exercise2)

        exercise3 = Exercise(name='Pull-up', description='Description of pull-up exercise.', instructions='Instructions for performing pull-up.', target_muscles='Back, Biceps')
        db.session.add(exercise3)

        exercise4 = Exercise(name='Deadlift', description='Description of deadlift exercise.', instructions='Instructions for performing deadlift.', target_muscles='Lower Back, Hamstrings, Glutes')
        db.session.add(exercise4)

        exercise5 = Exercise(name='Bench Press', description='Description of bench press exercise.', instructions='Instructions for performing bench press.', target_muscles='Chest, Shoulders, Triceps')
        db.session.add(exercise5)

        exercise6 = Exercise(name='Lunges', description='Description of lunges exercise.', instructions='Instructions for performing lunges.', target_muscles='Quadriceps, Hamstrings, Glutes')
        db.session.add(exercise6)

        exercise7 = Exercise(name='Dumbbell Row', description='Description of dumbbell row exercise.', instructions='Instructions for performing dumbbell row.', target_muscles='Back, Biceps')
        db.session.add(exercise7)

        exercise8 = Exercise(name='Leg Press', description='Description of leg press exercise.', instructions='Instructions for performing leg press.', target_muscles='Quadriceps, Hamstrings, Glutes')
        db.session.add(exercise8)

        exercise9 = Exercise(name='Shoulder Press', description='Description of shoulder press exercise.', instructions='Instructions for performing shoulder press.', target_muscles='Shoulders, Triceps')
        db.session.add(exercise9)

        exercise10 = Exercise(name='Plank', description='Description of plank exercise.', instructions='Instructions for performing plank.', target_muscles='Core')
        db.session.add(exercise10)

        exercise11 = Exercise(name='Russian Twist', description='Description of russian twist exercise.', instructions='Instructions for performing russian twist.', target_muscles='Obliques, Core')
        db.session.add(exercise11)

        exercise12 = Exercise(name='Crunches', description='Description of crunches exercise.', instructions='Instructions for performing crunches.', target_muscles='Abdominals')
        db.session.add(exercise12)

        exercise13 = Exercise(name='Barbell Curl', description='Description of barbell curl exercise.', instructions='Instructions for performing barbell curl.', target_muscles='Biceps')
        db.session.add(exercise13)

        exercise14 = Exercise(name='Tricep Dip', description='Description of tricep dip exercise.', instructions='Instructions for performing tricep dip.', target_muscles='Triceps')
        db.session.add(exercise14)

        exercise15 = Exercise(name='Leg Curl', description='Description of leg curl exercise.', instructions='Instructions for performing leg curl.', target_muscles='Hamstrings')
        db.session.add(exercise15)

        exercise16 = Exercise(name='Calf Raise', description='Description of calf raise exercise.', instructions='Instructions for performing calf raise.', target_muscles='Calves')
        db.session.add(exercise16)

        exercise17 = Exercise(name='Box Jump', description='Description of box jump exercise.', instructions='Instructions for performing box jump.', target_muscles='Legs')
        db.session.add(exercise17)

        exercise18 = Exercise(name='Bicycle Crunches', description='Description of bicycle crunches exercise.', instructions='Instructions for performing bicycle crunches.', target_muscles='Abdominals, Obliques')
        db.session.add(exercise18)

        exercise19 = Exercise(name='Chin-up', description='Description of chin-up exercise.', instructions='Instructions for performing chin-up.', target_muscles='Back, Biceps')
        db.session.add(exercise19)

        exercise20 = Exercise(name='Romanian Deadlift', description='Description of romanian deadlift exercise.', instructions='Instructions for performing romanian deadlift.', target_muscles='Hamstrings, Lower Back')
        db.session.add(exercise20)

        db.session.commit()

if __name__ == "__main__":
    initialize_database()
