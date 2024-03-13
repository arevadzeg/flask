from flask import request, jsonify, request
from app import app, db
from app.models import TrackingAndGoals
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime




@app.route('/tracking_and_goals', methods=['POST'])
@jwt_required()
def add_tracking_and_goals():
    data = request.json
    user_id = get_jwt_identity()
    date = datetime.strptime(data.get('date'), '%Y-%m-%d')
    weight = data.get('weight')
    fitness_goals = data.get('fitness_goals')
    achievements = data.get('achievements')

    tracking_and_goals = TrackingAndGoals(user_id=user_id, date=date, weight=weight, fitness_goals=fitness_goals, achievements=achievements)
    db.session.add(tracking_and_goals)
    db.session.commit()

    return jsonify({'message': 'Tracking and goals added successfully'}), 201

# Add routes for updating, deleting, and retrieving tracking and goals entries

@app.route('/tracking_and_goals', methods=['GET'])
@jwt_required()
def get_all_tracking_and_goals():
    user_id = get_jwt_identity()
    tracking_and_goals = TrackingAndGoals.query.filter_by(user_id=user_id).all()

    result = []
    for entry in tracking_and_goals:
        result.append({
            'id': entry.id,
            'user_id': entry.user_id,
            'date': entry.date,
            'weight': entry.weight,
            'fitness_goals': entry.fitness_goals,
            'achievements': entry.achievements
        })
    return jsonify(result), 200

@app.route('/tracking_and_goals/<int:entry_id>', methods=['GET'])
@jwt_required()
def get_tracking_and_goals(entry_id):
    user_id = get_jwt_identity()
    entry = TrackingAndGoals.query.filter_by(user_id=user_id,id=entry_id).first_or_404()
    
    return jsonify({
        'id': entry.id,
        'user_id': entry.user_id,
        'date': entry.date,
        'weight': entry.weight,
        'fitness_goals': entry.fitness_goals,
        'achievements': entry.achievements
    }), 200

@app.route('/tracking_and_goals/<int:entry_id>', methods=['PUT'])
@jwt_required()
def update_tracking_and_goals(entry_id):
    user_id = get_jwt_identity()
    entry = TrackingAndGoals.query.filter_by(user_id=user_id,id=entry_id).first_or_404()
    data = request.json
    if 'date' in data:
        entry.date = datetime.strptime(data['date'], '%Y-%m-%d')
    if 'weight' in data:
        entry.weight = data['weight']
    if 'fitness_goals' in data:
        entry.fitness_goals = data['fitness_goals']
    if 'achievements' in data:
        entry.achievements = data['achievements']
    db.session.commit()
    return jsonify({'message': 'Tracking and goals updated successfully'}), 200

@app.route('/tracking_and_goals/<int:entry_id>', methods=['DELETE'])
@jwt_required()
def delete_tracking_and_goals(entry_id):
    user_id = get_jwt_identity()
    entry = TrackingAndGoals.query.filter_by(user_id=user_id,id=entry_id).first_or_404()
    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message': 'Tracking and goals deleted successfully'}), 200