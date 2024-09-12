from flask_restful import Resource, reqparse
from models import Order, db
from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth(scheme='Bearer')

# Dictionnaire pour les tokens (pour simplifier, on utilise un token statique ici)
TOKENS = {
    "mysecrettoken": "taher"
}

@auth.verify_token
def verify_token(token):
    if token in TOKENS:
        return TOKENS[token]
    return None

parser = reqparse.RequestParser()
parser.add_argument('product_name', type=str)
parser.add_argument('quantity', type=int)
parser.add_argument('price', type=float)
parser.add_argument('order_date', type=str)

class OrderResource(Resource):
    @auth.login_required
    def get(self, order_id):
        order = Order.query.get_or_404(order_id)
        return {
            'id': order.id,
            'product_name': order.product_name,
            'quantity': order.quantity,
            'price': order.price,
            'order_date': order.order_date
        }

    @auth.login_required
    def put(self, order_id):
        args = parser.parse_args()
        order = Order(id=order_id, **args)
        db.session.add(order)
        db.session.commit()
        return {'message': 'Order created'}, 201

    @auth.login_required
    def patch(self, order_id):
        order = Order.query.get_or_404(order_id)
        args = parser.parse_args()
        for key, value in args.items():
            if value is not None:
                setattr(order, key, value)
        db.session.commit()
        return {'message': 'Order updated'}

    @auth.login_required
    def delete(self, order_id):
        order = Order.query.get_or_404(order_id)
        db.session.delete(order)
        db.session.commit()
        return {'message': 'Order deleted'}

class OrderSearchResource(Resource):
    @auth.login_required
    def get(self, product_name):
        orders = Order.query.filter(Order.product_name.like(f'%{product_name}%')).all()
        return [{'id': order.id, 'product_name': order.product_name} for order in orders]
