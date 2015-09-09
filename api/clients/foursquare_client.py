from api.helpers import *
import foursquare


class FoursquareClient:
    def __init__(self):
        self.config = json_from_file(os.path.join(os.path.dirname(__file__), '../config/foursquare.json'))
        self.client_id = self.config['client_id']
        self.client_secret = self.config['client_secret']
        self.client = foursquare.Foursquare(client_id=self.client_id, client_secret=self.client_secret)

    def search(self, location, number_of_places=5, interests=[]):
        return self.client.venues.search(params={
            'near': location,
            'limit': number_of_places,
            'query': list_to_csv(interests)
        })
