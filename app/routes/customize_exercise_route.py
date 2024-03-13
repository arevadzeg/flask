
from flask import request, jsonify, request
from app import app, db
from app.models import CustomExercise
from app.models import Exercise
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError

# CREATE
@app.route('/custom_exercises', methods=['POST'])
@jwt_required()
def create_custom_exercise():
    # Parse request data
    data = request.json
    exercise_id = data.get('exercise_id')

    # Check if the exercise exists
    Exercise.query.get_or_404(exercise_id)


    user_id = get_jwt_identity()
    repetitions = data.get('repetitions')
    sets = data.get('sets')
    duration = data.get('duration')
    distance = data.get('distance')

    # Validate request data
    if user_id is None:
        return jsonify({'error': 'User ID is required.'}), 400
    if repetitions is None and sets is None and duration is None and distance is None:
        return jsonify({'error': 'At least one of repetitions, sets, duration, or distance must be provided.'}), 400

    # Create a custom exercise
    custom_exercise = CustomExercise(
        user_id=user_id,
        exercise_id=exercise_id,
        repetitions=repetitions,
        sets=sets,
        duration=duration,
        distance=distance
    )

    # Add custom exercise to the database
    db.session.add(custom_exercise)

    # Commit changes to the database
    try:
        db.session.commit()
        return jsonify({'message': 'Custom exercise created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Failed to create custom exercise. Please check your data.'}), 400


# UPDATE
@app.route('/custom_exercises/<int:exercise_id>', methods=['PUT'])
@jwt_required()
def update_custom_exercise(exercise_id):
    # Check if the custom exercise exists
    custom_exercise = CustomExercise.query.get_or_404(exercise_id)

    # Ensure that the user owns the custom exercise
    current_user_id = get_jwt_identity()
    if custom_exercise.user_id != current_user_id:
        return jsonify({'error': 'Unauthorized access to the custom exercise.'}), 403

    # Parse request data
    data = request.json
    repetitions = data.get('repetitions')
    sets = data.get('sets')
    duration = data.get('duration')
    distance = data.get('distance')

    # Validate request data
    if repetitions is None and sets is None and duration is None and distance is None:
        return jsonify({'error': 'At least one of repetitions, sets, duration, or distance must be provided.'}), 400

    # Update the custom exercise
    if repetitions is not None:
        custom_exercise.repetitions = repetitions
    if sets is not None:
        custom_exercise.sets = sets
    if duration is not None:
        custom_exercise.duration = duration
    if distance is not None:
        custom_exercise.distance = distance

    # Commit changes to the database
    try:
        db.session.commit()
        return jsonify({'message': 'Custom exercise updated successfully'}), 200
    except:
        db.session.rollback()
        return jsonify({'message': 'Failed to update custom exercise. Please try again later.'}), 500


# GET ALL CUSTOM EXERCICES
@app.route('/custom_exercises', methods=['GET'])
@jwt_required()
def get_custom_exercises():
    # Get the user ID from the JWT token
    user_id = get_jwt_identity()

    # Query all custom exercises for the user
    custom_exercises = CustomExercise.query.filter_by(user_id=user_id).all()

    # Serialize the custom exercises
    serialized_custom_exercises = [{
        'id': exercise.id,
        'exercise_id': exercise.exercise_id,
        'repetitions': exercise.repetitions,
        'sets': exercise.sets,
        'duration': exercise.duration,
        'distance': exercise.distance
    } for exercise in custom_exercises]

    return jsonify({'custom_exercises': serialized_custom_exercises}), 200


# DELETE
@app.route('/custom_exercises/<int:exercise_id>', methods=['DELETE'])
@jwt_required()
def delete_custom_exercise(exercise_id):
    # Check if the custom exercise exists
    user_id = get_jwt_identity()
    custom_exercise = CustomExercise.query.filter_by(user_id=user_id,id=exercise_id).first_or_404()

    # Ensure that the user owns the custom exercise
    current_user_id = get_jwt_identity()
    if custom_exercise.user_id != current_user_id:
        return jsonify({'error': 'Unauthorized access to the custom exercise.'}), 403

    # Delete the custom exercise
    db.session.delete(custom_exercise)

    # Commit changes to the database
    try:
        db.session.commit()
        return jsonify({'message': 'Custom exercise deleted successfully'}), 200
    except:
        db.session.rollback()
        return jsonify({'message': 'Failed to delete custom exercise. Please try again later.'}), 500