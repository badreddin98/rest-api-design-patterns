from flask import Blueprint, request, jsonify
from models import db, Product

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    
    if not all(key in data for key in ['name', 'price']):
        return jsonify({'error': 'Missing required fields'}), 400
        
    new_product = Product(
        name=data['name'],
        price=data['price']
    )
    
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify({
        'id': new_product.id,
        'name': new_product.name,
        'price': new_product.price
    }), 201

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': prod.id,
        'name': prod.name,
        'price': prod.price
    } for prod in products])
