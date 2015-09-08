import json
from api.clients.foursquare_client import FoursquareClient
from api.places.places_list import PlacesList


class CircuitsResource:
    def on_get(self, request, response, location, number_of_places=5, interests=['coffee']):
        foursquare_response = FoursquareClient().search(location, number_of_places, interests)

        places = PlacesList()
        for venue in foursquare_response['venues']:
            places.extend([{
                'location': venue['location'],
                'name': venue['name']
            }])

        # TODO: pass the list of places through the algorithm to generate a circuit
        # TODO: get current location
        places.order({
            'location': {
                'lat': 41.14870842690923,
                'lng': -8.61085212647548
            }
        })

        response.body = json.dumps(places, separators=(',', ':'))
