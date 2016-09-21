import googlemaps
import json
import os


class GoogleMapsClient:
    def __init__(self):
        self.config = json.load(open(os.path.join(os.path.dirname(__file__), '../config/googlemaps.json'), 'r'))
        self.key = self.config['key']
        self.client = googlemaps.Client(self.key)

    def distance_between(self, p1, p2):
        result = self.client.distance_matrix(p1, p2)
        return result['rows'][0]['elements'][0]['distance']['value']
