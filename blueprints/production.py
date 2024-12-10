from flask import Blueprint, request, jsonify
from models import db, Production
from datetime import datetime

production_bp = Blueprint('production', __name__)

@production_bp.route('/production', methods=['POST'])
def create_production():
    data = request.get_json()
    
    if not all(key in data for key in ['product_id', 'quantity_produced']):
        return jsonify({'error': 'Missing required fields'}), 400
        
    new_production = Production(
        product_id=data['product_id'],
        quantity_produced=data['quantity_produced'],
        date_produced=datetime.now().date()
    )
    
    db.session.add(new_production)
    db.session.commit()
    
    return jsonify({
        'id': new_production.id,
        'product_id': new_production.product_id,
        'quantity_produced': new_production.quantity_produced,
        'date_produced': new_production.date_produced.isoformat()
    }), 201

@production_bp.route('/production', methods=['GET'])
def get_production():
    productions = Production.query.all()
    return jsonify([{
        'id': prod.id,
        'product_id': prod.product_id,
        'quantity_produced': prod.quantity_produced,
        'date_produced': prod.date_produced.isoformat()
    } for prod in productions])
