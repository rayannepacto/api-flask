from flask_restful import Resource
from flask import jsonify

purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido número 1',
        'items': [
            {
                'id': 1,
                'description': 'Item número 1',
                'price': 20.99
            }
        ]

    }

]


class PurchcaseOrders(Resource):
    def get(self):
        return jsonify(purchase_orders)



