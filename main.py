from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from datetime import datetime


app = Flask(__name__)
api = Api(app)

temperature_post_args = reqparse.RequestParser()
temperature_post_args.add_argument('temperature', type=float, help="temperature required", required=True)
temperature_post_args.add_argument('created_at', type=str, help="created time required", required=True)

temperatures = []

@app.route('/api/v1/temperature/<string:user_id>', methods=['POST'])
def add_temperature(user_id):
    print(user_id)
    args = temperature_post_args.parse_args()
    if request.method == 'POST':
        temperature = {
            'id': user_id,
            'temperature': args['temperature'],
            'created_at': args['created_at']
        }
        temperatures.append(temperature)
        return temperature, 201

@app.route('/api/v1/temperature', methods=['GET'])
def getTemperatures():
    if request.method == 'GET':
        return {'payload': temperatures}, 200

if __name__ == "__main__":
    app.run(debug=True)