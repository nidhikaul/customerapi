#!/usr/bin/env python3
# encoding: utf-8

from flask import Flask, jsonify, request
from getCustomer import get_customer
from updateCustomer import purchase_item
from addCustomer import create_customer 
from deleteCustomer import delete_customer

app = Flask(__name__)

#GET customer API
@app.route('/customers', methods=['GET'])
def query_records():
    name = request.args.get('name', type=str)
    result = get_customer(name)

    if result != None:
        return jsonify(result)
    else:
        return jsonify({'error': 'data not found'}) , 400

#PUT purchase for a customer API
@app.route('/purchases/<name>', methods=['PUT'])
def update_record(name):
    result = purchase_item(name)

    if result != None:
        return jsonify(result)
    else:
        return jsonify({'error': 'data not found'}), 400

#POST new customer API (with no name)
@app.route('/new/', methods=['POST'])
def create_record_error():
    return jsonify({'error': 'Enter customer name'}), 400

#POST new customer API
@app.route('/new/<name>', methods=['POST'])
def create_record(name):
    print(f"create_record: name={name}")
    result = create_customer(name)
    print(result)

    if result != None:
        return jsonify(result)
    else:
        return jsonify({'error': 'customer already exists or name is invalid'}), 422

#DELETE existing customer API
@app.route('/customers/<name>', methods=['DELETE'])
def delete_record(name):
    result = delete_customer(name)

    if result != None:
        return jsonify(result)
    else:
        return jsonify({'error': 'data not found'}), 400

app.run(debug=True)