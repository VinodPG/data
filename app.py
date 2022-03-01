from flask import Flask, jsonify, request
from flask_restx import Api, Resource, Namespace
from config import app, db
import pandas as pd

api = Api(app)

@api.route('/product')
class Product(Resource):
    
    def get(self):
  
        return jsonify({'message': 'hello world'})
  
    # Corresponds to POST request
    def post(self):
          
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201
  
  
# driver function
if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
