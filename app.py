from flask from Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    #methods go here
    pass


class Locations(Resources):
    #methods go here
    pass

api.add_resource(Users, '/users') # '/users' is our entry point for Users
api.add_resource(Locations, '/locations') # and '/locations' iis our entry point
