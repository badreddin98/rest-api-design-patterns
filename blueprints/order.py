from flask import Blueprint, request, jsonify
from models import db, Order, Product

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    
    if not all(key in data for key in ['customer_id', 'product_id', 'quantity']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Calculate total price
    product = Product.query.get(data['product_id'])
    if not product:
        return jsonify({'error': 'Product not found'}), 404
        
    total_price = product.price * data['quantity']
    
    new_order = Order(
        customer_id=data['customer_id'],
        product_id=data['product_id'],
        quantity=data['quantity'],
        total_price=total_price
    )
    
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify({
        'id': new_order.id,
        'customer_id': new_order.customer_id,
        'product_id': new_order.product_id,
        'quantity': new_order.quantity,
        'total_price': new_order.total_price
    }), 201

@order_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{
        'id': order.id,
        'customer_id': order.customer_id,
        'product_id': order.product_id,
        'quantity': order.quantity,
        'total_price': order.total_price
    } for order in orders])
