from flask import Flask, jsonify

from flask_restful import Api

from purchase_orders.resources import PurchcaseOrders


app = Flask(__name__)
api = Api(app)


api.add_resource(PurchcaseOrders, '/purchase_orders')
app.run(port=5000)
