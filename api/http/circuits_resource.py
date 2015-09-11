import json
from api.clients.foursquare_client import FoursquareClient
from api.models.places_list import PlacesList
from api.models.places import Place


class CircuitsResource:
    def on_get(self, request, response, location, interests, number_of_places=5):
        foursquare_response = FoursquareClient().search(location, number_of_places, interests)

        location = location.split(',')
        location = {
            'location': {
                'lat': float(location[0]),
                'lng': float(location[1])
            }
        }

        initial_place = Place("", location[0], location[1])

        places = PlacesList()
        for venue in foursquare_response['venues']:
            venue_location = venue['location']
            places.extend([Place(venue['name'], location['lat'], location['lng'])])

        # places = PlacesList()
        # for venue in foursquare_response['venues']:
        #     places.extend([{
        #         'location': venue['location'],
        #         'name': venue['name']
        #     }])

        places.tripify(location)

        response.body = json.dumps(places, separators=(',', ':'))
        response.set_header('Access-Control-Allow-Origin', '*')
