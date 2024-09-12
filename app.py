from flask import Flask
from flask_restful import Api
from models import db
from resources import OrderResource, OrderSearchResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

# Création des tables
with app.app_context():
    db.create_all()

# Routes de l'API
api.add_resource(OrderResource, '/order/<int:order_id>')
api.add_resource(OrderSearchResource, '/ordersearch/<string:product_name>')

if __name__ == '__main__':
    app.run(debug=True)
