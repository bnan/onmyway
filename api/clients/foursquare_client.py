import json
import os
from api.helpers import *
import foursquare

class FoursquareClient:
    def __init__(self):
        config = json_from_file(os.path.join(os.path.dirname(__file__), '../config/foursquare.json'))

        self.client = foursquare.Foursquare(
            client_id = config['client_id'],
            client_secret = config['client_secret']
        )

    def search(self, location, number_of_places = 5, interests = []):
        return self.client.venues.search(params = {
            'near': location,
            'limit': number_of_places,
            'query': list_to_csv(interests)
        })
