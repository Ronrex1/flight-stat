from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['flightdb']
flights_collection = db['flights']

@app.route('/api/flights', methods=['GET'])
def get_flights():
    flights = list(flights_collection.find({}, {'_id': 0}))
    return jsonify(flights)

if __name__ == '__main__':
    app.run(debug=True)
