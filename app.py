#!/usr/bin/python3
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast


app = Flask(__name__)
api = Api(app)


class Users(Resource):
    #methods go here
    def get(self):
        data = pd.read_csv('users.csv') #read csv
        data = data.to_dict() #conert dataframe to dictionary
        return {'data':data}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('userId', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)

        args = parser.parse_args()

        # create new dataframe containing new values
        new_data = pd.DataFrame({
            'userId': args['userId'],
            'name': args['name'],
            'city': args['city'],
            'locations': [[]]
        })

        # read our CSV
        data = pd.read_csv('users.csv')
        # add the newly provided values
        data = data.append(new_data, ignore_index=True)
        # save back to csv
        data.to_csv()
        return {'data': data.to_dict()}, 200



class Locations(Resource):
    #methods go here
    def get(self):
        data = pd.read_csv('locations.csv')
        data = data.to_dict()
        return {'data':data}, 200


api.add_resource(Users, '/users') # '/users' is our entry point for Users
api.add_resource(Locations, '/locations') # and '/locations' iis our entry point

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
