from flask_restful import Api, Resource, reqparse
import requests

PLACES_API_BASE_URL = 'https://storage.googleapis.com/coding-session-rest-api/'
class PlacesApiHandler(Resource):
  def get(self,placeid):
    responsePlace = requests.get(PLACES_API_BASE_URL+placeid)
    placeData= responsePlace.json()
    return {
    
      'displayed_what':placeData.get("displayed_what"),
      'displayed_where':placeData.get("displayed_where"),
      'opening_hours':placeData.get("opening_hours")

      }

  