#!/usr/bin/env python3

from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'products': [
                'Ice cream',
                'Chocolate',
                'Fruit'
            ]
        }

api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
