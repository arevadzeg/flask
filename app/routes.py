from flask import request, jsonify, Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app import app, db
from app.models import User
from app.models import WorkoutPlan


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid username or password'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200




# app = Blueprint('workout_plans', __name__)

@app.route('/workout_plans', methods=['POST'])
def create_workout_plan():
    
    print('asdasd')
    data = request.json

    user_id = data.get('user_id')
    frequency = data.get('frequency')
    goals = data.get('goals')
    session_duration = data.get('session_duration')

    print('asdasd')
    workout_plan = WorkoutPlan(user_id=user_id, frequency=frequency, goals=goals, session_duration=session_duration)
    print('asdasd',workout_plan )
    db.session.add(workout_plan)
    db.session.commit()

    return jsonify({'message': 'Workout plan created successfully'}), 201

@app.route('/workout_plans/<int:plan_id>', methods=['GET'])
def get_workout_plan(plan_id):
    workout_plan = WorkoutPlan.query.get_or_404(plan_id)
    return jsonify({
        'id': workout_plan.id,
        'user_id': workout_plan.user_id,
        'frequency': workout_plan.frequency,
        'goals': workout_plan.goals,
        'session_duration': workout_plan.session_duration
        # Add more fields as needed
    })


@app.route('/workout_plans/<int:plan_id>', methods=['PUT'])
def update_workout_plan(plan_id):
    workout_plan = WorkoutPlan.query.get_or_404(plan_id)
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
def get_all_workout_plans():
    workout_plans = WorkoutPlan.query.all()
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
def delete_workout_plan(plan_id):
    workout_plan = WorkoutPlan.query.get_or_404(plan_id)
    db.session.delete(workout_plan)
    db.session.commit()
    return jsonify({'message': 'Workout plan deleted successfully'}), 200
