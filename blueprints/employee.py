from flask import Blueprint, request, jsonify
from models import db, Employee
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    
    if not all(key in data for key in ['name', 'position']):
        return jsonify({'error': 'Missing required fields'}), 400
        
    new_employee = Employee(
        name=data['name'],
        position=data['position']
    )
    
    db.session.add(new_employee)
    db.session.commit()
    
    return jsonify({
        'id': new_employee.id,
        'name': new_employee.name,
        'position': new_employee.position
    }), 201

@employee_bp.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([{
        'id': emp.id,
        'name': emp.name,
        'position': emp.position
    } for emp in employees])
