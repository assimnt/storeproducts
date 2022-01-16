from flask import Flask, request, jsonify
from flask_restx import Api, Resource , reqparse

from sql_connection import get_sql_connection
import mysql.connector
import json

import products_data_access_object
import order
import measurement

app = Flask(__name__)

api = Api(app)

parser = reqparse.RequestParser()

connection = get_sql_connection()

@api.route('/getmeasurement')
class project(Resource):
    @api.doc(parser=parser)
    def get_measurement():
        response = measurement.get_productmeasurements(connection)
        response = jsonify(response)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, getmeasurement \
               @api.route('/getProducts_data_access_object/<string:id>')
        def get_products():
            response = products_data_access_object.get_all_products(connection)
            response = jsonify(response)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response,getProducts_data_access_object \
                   @api.route('/insertProduct /<string:id>')
            def insert_product():

                args = parser.parse_args()
                post_var1 = args['data']
                product_id = products_data_access_object.insert_new_product(connection, post_var1)
                response = jsonify({
        'product_id': product_id})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response ,insertProduct, + post_var1 + id  \
               @api.route('/getAllOrders')
        def get_all_orders():
            response = order.get_all_orders(connection)
            response = jsonify(response)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, getallOrders\
                   @api.route('/insertOrder /<string:id>')
            def insert_order():
                args = parser.parse_args()
                post_var2 = args['data']

                order_id = order.insert_order(connection, post_var2)
                response = jsonify({
                    'order_id': order_id})
                response.headers.add('Access-Control-Allow-Origin', '*')
                return response, insert_order + post_var2 + id\
                       @api.route('/deleteProduct')
                def delete_product():


                    return_id = products_data_access_object.delete_product(connection, request.form['product_id'])
                    response = jsonify({
                        'product_id': return_id
                    })
                    response.headers.add('Access-Control-Allow-Origin', '*')
                    return response ,deleteProduct
                    return 'project'
                    if __name__ == "__main__":
                        print("product shop")
                        app.run()