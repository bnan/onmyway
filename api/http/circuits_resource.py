import json
from api.clients.foursquare_client import FoursquareClient
from api.models.places_list import PlacesList


class CircuitsResource:
    def on_get(self, request, response, location, interests, number_of_places=5):
        foursquare_response = FoursquareClient().search(location, number_of_places, interests)

        location = location.split(',')
        location = {
            'location': {
                'lat': location[0],
                'lng': location[1]
            }
        }

        places = PlacesList()
        for venue in foursquare_response['venues']:
            places.extend([{
                'location': venue['location'],
                'name': venue['name']
            }])

        # TODO: pass the list of places through the algorithm to generate a circuit
        # TODO: get current location
        places.tripify(location)

        response.body = json.dumps(places, separators=(',', ':'))
        response.set_header('Access-Control-Allow-Origin', '*')
