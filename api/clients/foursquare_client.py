import foursquare
import json
import os


class FoursquareClient:
    def __init__(self):
        self.config = json.load(open(os.path.join(os.path.dirname(__file__), '../config/foursquare.json'), 'r'))
        self.client_id = self.config['client_id']
        self.client_secret = self.config['client_secret']
        self.client = foursquare.Foursquare(client_id=self.client_id, client_secret=self.client_secret)

    def search(self, location, number_of_places=5, interests=[]):
        return self.client.venues.search(params={
            'near': location,
            'limit': number_of_places,
            'query': list_to_csv(interests)
        })

def list_to_csv(a):
    return ','.join(map(str, list(a)))
