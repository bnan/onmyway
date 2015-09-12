import json
from api.clients.foursquare_client import FoursquareClient
from api.clients.googlemaps_client import GoogleMapsClient
from api.models.places_list import PlacesList
from api.models.place import Place


class CircuitsResource:
    def on_get(self, request, response, current_location, interests, number_of_places=5):
        venues = FoursquareClient().search(current_location, number_of_places, interests)['venues']

        current_location = current_location.split(',')
        current_location = Place('', float(current_location[0]), float(current_location[1]), '', '')

        places = PlacesList()
        for venue in venues:
            venue_name = venue['name']
            venue_location = venue['location']
            venue_icon = venue['categories'][0]['icon']['prefix'] + 'bg_32' + venue['categories'][0]['icon']['suffix']
            venue_hours = venue['hours']
            places.extend([Place(venue_name, float(venue_location['lat']), float(venue_location['lng']), venue_icon, venue_hours)])

        snap_to_roads(places)

        places.tripify(current_location)

        response.body = json.dumps(places.__dict__(), separators=(',', ':'))
        response.set_header('Access-Control-Allow-Origin', '*')


def snap_to_roads(places):
    lat_lng = [(place.get_lat(), place.get_lng()) for place in places]
    results = GoogleMapsClient().client.snap_to_roads(lat_lng)
    for result in results:
        place = places[result['originalIndex']]
        place.set_lat(result['location']['latitude'])
        place.set_lng(result['location']['longitude'])
    return places
