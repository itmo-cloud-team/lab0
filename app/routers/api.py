from flask import Blueprint, request, jsonify
import db

router = Blueprint('api', __name__)

@router.get('/api/list')
def list():
    aircraft = db.list_aircraft()
    return jsonify({'count': len(aircraft), 'fleet': aircraft})

@router.post('/api/enlist')
def enlist():
    data = request.get_json()
    tail_number = data['tailNumber']
    production_date = data['productionDate']
    aircraft_type = data['icaoAircraftType']
    if tail_number not in [x['tailNumber'] for x in db.list_aircraft()]:
        if db.enlist_aircraft(tail_number, production_date, aircraft_type):
            return jsonify({'status': 'OK'}), 201
        else:
            return jsonify({'status': 'FAIL', 'reason': 'Server error.'}), 503
    else:
        return jsonify({'status': 'FAIL', 'reason': 'Already exists.'}), 409

