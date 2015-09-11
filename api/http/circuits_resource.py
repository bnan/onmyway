import json
from api.clients.foursquare_client import FoursquareClient
from api.models.places_list import PlacesList
from api.models.place import Place


class CircuitsResource:
    def on_get(self, request, response, location, interests, number_of_places=5):
        venues = FoursquareClient().search(location, number_of_places, interests)['venues']

        location = location.split(',')
        location = Place('', float(location[0]), float(location[1]))

        places = PlacesList()
        for venue in venues:
            venue_name = venue['name']
            venue_location = venue['location']
            places.extend([Place(venue_name, float(venue_location['lat']), float(venue_location['lng']))])

        places.tripify(location)

        response.body = json.dumps(places.__dict__(), separators=(',', ':'))
        response.set_header('Access-Control-Allow-Origin', '*')
