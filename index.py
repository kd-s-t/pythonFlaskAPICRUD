from flask import Flask, jsonify, request
from flask_cors import CORS
from pprint import pprint
import os
import database.database as db

import controller.Users as crud

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def home():
    return jsonify({
    	"status": "success",
        "message": "Welcome to Flask API"
    })

@app.route("/users/create", methods=['POST'])
def create():
   
    name = request.form['name']
    address = request.form['address']

    api = crud.Users()
    api.create(name, address)

    return jsonify({
    	"status": "success",
    	"messge": "User created",
    })

@app.route("/users/<int:id>", methods=['GET'])
def user(id):
    api  = crud.Users()
    user = api.get(id)

    return jsonify({
    	"status": "success",
    	"user": user
    })

@app.route("/users", methods=['GET'])
def users():
    api   = crud.Users()
    users = api.read()

    return jsonify({
    	"status": "success",
    	"users": users
    })

@app.route("/users/<int:id>/update", methods=['POST'])
def update(id):
    name = request.form['name']
    address = request.form['address']

    api  = crud.Users()
    user = api.update(id, name, address)

    return jsonify({
    	"status": "success",
    	"user": user
    })

@app.route("/users/<int:id>/delete", methods=['GET'])
def delete(id):
    api  = crud.Users()
    user = api.delete(id)

    return jsonify({
        "status": "Successfully deleted user",
        "user": user
    })

@app.route("/migrate", methods=['GET'])
def migrate():
    connection = db.Database('python_flask_api_crudv2')
    connection.setLocalhost('localhost')
    connection.setUsername('root')
    connection.setPassword('root')
    connection.createDatabase()

    connection.setTableName('customers')
    connection.createTable()

    return jsonify({
        "status": "success"
    })


if __name__ == '__main__':
	app.run(debug=True)
