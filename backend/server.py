from flask import Flask, jsonify, request
from util import is_dag
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

# Define a route for the home page
@app.route('/')
def home():
    return "Hello, Flask!"


# Define a route to handle POST requests
@app.route('/pipelines/parse', methods=['POST'])
def post_data():
    data = request.json  # Get JSON data from the request

    response = {
        'status': 'parsed',
        'nodeSize': data['node'],  # Accessing nodes using dictionary keys
        'edgeSize': len(data['edge']),  # Accessing edges using dictionary keys
        'isDAG': is_dag(data['edge']),  # Passing edges to the is_dag function
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
