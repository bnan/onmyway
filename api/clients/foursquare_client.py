import foursquare
import json
import os


class FoursquareClient:
    def __init__(self):
        self.config = json.load(open(os.path.join(os.path.dirname(__file__), '../config/foursquare.json'), 'r'))
        self.client_id = self.config['client_id']
        self.client_secret = self.config['client_secret']
        self.client = foursquare.Foursquare(client_id=self.client_id, client_secret=self.client_secret)
        self.categories = {
            'entertainment': '4d4b7104d754a06370d81259',
            'museum': '4bf58dd8d48988d181941735',
            'theater': '4bf58dd8d48988d137941735',
            'food': '4d4b7105d754a06374d81259',
            'coffee': '4bf58dd8d48988d1e0931735',
            'nightlife': '4d4b7105d754a06376d81259',
            'outdoors': '4d4b7105d754a06377d81259',
            'shopping': '4bf58dd8d48988d1fd941735,50be8ee891d4fa8dcc7199a7'
        }

    def search(self, location, number_of_places=5, interests=''):
        try:
            return self.client.venues.search(params={
                'near': location,
                'limit': number_of_places,
                'categoryId': ','.join([self.categories[category] for category in interests.split(',')]),
                'radius': 4999
            })
        except:
            return {'venues': []}
