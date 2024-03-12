
from flask import request, jsonify, request
from app import app, db
from app.models import WorkoutPlan
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route('/workout_plans', methods=['POST'])
@jwt_required()
def create_workout_plan():
    data = request.json
    user_id = get_jwt_identity()
    frequency = data.get('frequency')
    goals = data.get('goals')
    session_duration = data.get('session_duration')

    workout_plan = WorkoutPlan(user_id=user_id, frequency=frequency, goals=goals, session_duration=session_duration)
    db.session.add(workout_plan)
    db.session.commit()

    return jsonify({'message': 'Workout plan created successfully'}), 201

@app.route('/workout_plans/<int:plan_id>', methods=['GET'])
@jwt_required()
def get_workout_plan(plan_id):
    user_id = get_jwt_identity()

    workout_plan = WorkoutPlan.query.filter_by(id=plan_id, user_id=user_id).first_or_404()

    return jsonify({
        'id': workout_plan.id,
        'user_id': workout_plan.user_id,
        'frequency': workout_plan.frequency,
        'goals': workout_plan.goals,
        'session_duration': workout_plan.session_duration
    })

@app.route('/workout_plans/<int:plan_id>', methods=['PUT'])
@jwt_required()
def update_workout_plan(plan_id):
    user_id = get_jwt_identity()
    workout_plan = WorkoutPlan.query.filter_by(id=plan_id, user_id=user_id).first_or_404()
    data = request.json
    # Update fields if provided in the request data
    if 'frequency' in data:
        workout_plan.frequency = data['frequency']
    if 'goals' in data:
        workout_plan.goals = data['goals']
    if 'session_duration' in data:
        workout_plan.session_duration = data['session_duration']
    # Update the workout plan in the database
    db.session.commit()
    return jsonify({'message': 'Workout plan updated successfully'}), 200


@app.route('/workout_plans', methods=['GET'])
@jwt_required()
def get_all_workout_plans():
    user_id = get_jwt_identity()
    workout_plans = WorkoutPlan.query.filter_by(user_id=user_id).first_or_404()

    # Serialize the workout plans into JSON format
    result = []
    for workout_plan in workout_plans:
        result.append({
            'id': workout_plan.id,
            'user_id': workout_plan.user_id,
            'frequency': workout_plan.frequency,
            'goals': workout_plan.goals,
            'session_duration': workout_plan.session_duration
            # Add more fields as needed
        })
    return jsonify(result), 200


@app.route('/workout_plans/<int:plan_id>', methods=['DELETE'])
@jwt_required()
def delete_workout_plan(plan_id):
    user_id = get_jwt_identity()
    workout_plan = WorkoutPlan.query.filter_by(id=plan_id, user_id=user_id).first_or_404()
    db.session.delete(workout_plan)
    db.session.commit()
    return jsonify({'message': 'Workout plan deleted successfully'}), 200

