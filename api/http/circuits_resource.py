import json
from api.clients.foursquare_client import FoursquareClient
from api.clients.googlemaps_client import GoogleMapsClient
from api.models.places_list import PlacesList
from api.models.place import Place

maps_to_generate = 3


class CircuitsResource:
    @staticmethod
    def on_get(request, response, current_location, interests, number_of_places=5):
        number_of_places = int(number_of_places)
        venues = FoursquareClient().search(current_location, number_of_places * maps_to_generate, interests)['venues']

        current_location = current_location.split(',')
        current_location = Place('', float(current_location[0]), float(current_location[1]), '')

        i, places = 0, []
        while i < maps_to_generate:
            places += [PlacesList()]
            for venue in venues[i * number_of_places:i * number_of_places + number_of_places]:
                venue_name = venue['name']
                venue_location = venue['location']
                venue_icon = venue['categories'][0]['icon']['prefix'] + 'bg_32' + venue['categories'][0]['icon'][
                    'suffix']

                places[i].extend(
                    [Place(venue_name, float(venue_location['lat']), float(venue_location['lng']), venue_icon)])

            snap_to_roads(places[i])
            places[i].tripify(current_location)

            i += 1

        response.body = json.dumps([place.__dict__() for place in places], separators=(',', ':'))
        response.set_header('Access-Control-Allow-Origin', '*')


def snap_to_roads(places):
    lat_lng = [(place.get_lat(), place.get_lng()) for place in places]
    try:
        results = GoogleMapsClient().client.snap_to_roads(lat_lng)
        for result in results:
            place = places[result['originalIndex']]
            place.set_lat(result['location']['latitude'])
            place.set_lng(result['location']['longitude'])
    except:
        pass
