import json

from api.circuits.circuits_foursquare import CircuitsFoursquare
from api.places.places_list import PlacesList


class CircuitsResource:
    def on_get(self, request, response, location='Porto', number_of_places=5, interests=['coffee']):
        foursquare_response = CircuitsFoursquare().search(location, number_of_places, interests)

        places = PlacesList()
        for venue in foursquare_response['venues']:
            places.extend([{
                'location': venue['location'],
                'name': venue['name']
            }])

        # TODO: pass the list of places through the algorithm to generate a circuit
        # places.sort()

        response.body = json.dumps(places, separators=(',', ':'))
