from flask import request, jsonify, request
from app import app, db
from app.models import TrackingAndGoals


@app.route('/tracking_and_goals', methods=['POST'])
def add_tracking_and_goals():
    data = request.json
    user_id = data.get('user_id')
    date = data.get('date')
    weight = data.get('weight')
    fitness_goals = data.get('fitness_goals')
    achievements = data.get('achievements')

    tracking_and_goals = TrackingAndGoals(user_id=user_id, date=date, weight=weight, fitness_goals=fitness_goals, achievements=achievements)
    db.session.add(tracking_and_goals)
    db.session.commit()

    return jsonify({'message': 'Tracking and goals added successfully'}), 201

# Add routes for updating, deleting, and retrieving tracking and goals entries

@app.route('/tracking_and_goals', methods=['GET'])
def get_all_tracking_and_goals():
    tracking_and_goals = TrackingAndGoals.query.all()
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
def get_tracking_and_goals(entry_id):
    entry = TrackingAndGoals.query.get_or_404(entry_id)
    return jsonify({
        'id': entry.id,
        'user_id': entry.user_id,
        'date': entry.date,
        'weight': entry.weight,
        'fitness_goals': entry.fitness_goals,
        'achievements': entry.achievements
    }), 200

@app.route('/tracking_and_goals/<int:entry_id>', methods=['PUT'])
def update_tracking_and_goals(entry_id):
    entry = TrackingAndGoals.query.get_or_404(entry_id)
    data = request.json
    if 'date' in data:
        entry.date = data['date']
    if 'weight' in data:
        entry.weight = data['weight']
    if 'fitness_goals' in data:
        entry.fitness_goals = data['fitness_goals']
    if 'achievements' in data:
        entry.achievements = data['achievements']
    db.session.commit()
    return jsonify({'message': 'Tracking and goals updated successfully'}), 200

@app.route('/tracking_and_goals/<int:entry_id>', methods=['DELETE'])
def delete_tracking_and_goals(entry_id):
    entry = TrackingAndGoals.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message': 'Tracking and goals deleted successfully'}), 200