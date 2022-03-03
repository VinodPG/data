from flask import Flask, jsonify, request
from flask_restx import Api, Resource, Namespace
from config import app, db
from models import Products
import pandas as pd
# import numpy as np

api = Api(app)

@api.route('/product')
class Product(Resource):
    
    def get(self):
        products = db.session.query(Products).all()
        return jsonify({'data': products})
  
    # Corresponds to POST request
    def post(self):
        df = pd.read_csv('data/products.csv')  
        df = df.astype('object').mask(pd.isna, None)
        records=df.to_dict('records')
        # print("Records - " + str(records))
        db.session.bulk_insert_mappings(Products, records, render_nulls=True)
        db.session.commit()
        return jsonify({'status': 'success'}), 200
  
  
# driver function
if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
