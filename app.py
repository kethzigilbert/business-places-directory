from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from api.PlacesApiHandler import PlacesApiHandler

app = Flask(__name__)
CORS(app) 
api = Api(app)



api.add_resource(PlacesApiHandler, '/places/<string:placeid>')