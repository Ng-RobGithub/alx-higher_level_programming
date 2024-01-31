#!/usr/bin/python3

from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def index():
    return 'Hello, world!'

# Define a route for /route_1
@app.route('/route_1')
def route_1():
    return 'Route 1'

# Define a route for /route_2
@app.route('/route_2')
def route_2():
    return 'Route 2'

# Define a route for /route_3 that accepts GET and DELETE requests
@app.route('/route_3', methods=['GET', 'DELETE'])
def route_3():
    if request.method == 'GET':
        return 'Route 3 - GET request received'
    elif request.method == 'DELETE':
        return 'Route 3 - DELETE request received'

# Define a route for /route_4
@app.route('/route_4')
def route_4():
    return 'Route 4'

# Define a route for /route_5
@app.route('/route_5')
def route_5():
    return 'route 5'

# Define a route for /route_6
@app.route('/route_6', methods=['POST'])
def route_6():
    return 'Route 6 - POST request received'

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
