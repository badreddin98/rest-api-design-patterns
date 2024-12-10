from flask import Blueprint, request, jsonify
from models import db, Customer

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    
    if not all(key in data for key in ['name', 'email', 'phone']):
        return jsonify({'error': 'Missing required fields'}), 400
        
    new_customer = Customer(
        name=data['name'],
        email=data['email'],
        phone=data['phone']
    )
    
    db.session.add(new_customer)
    db.session.commit()
    
    return jsonify({
        'id': new_customer.id,
        'name': new_customer.name,
        'email': new_customer.email,
        'phone': new_customer.phone
    }), 201

@customer_bp.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{
        'id': cust.id,
        'name': cust.name,
        'email': cust.email,
        'phone': cust.phone
    } for cust in customers])
