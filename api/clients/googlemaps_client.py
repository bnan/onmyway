import googlemaps


class GoogleMapsClient:
    def __init__(self):
        self.key = 'AIzaSyCITlqVIMJwHvEDJ9vRGeeWLqibnARlUBo'
        self.client = googlemaps.Client(self.key)

    def distance_between(self, p1, p2):
        result = self.client.distance_matrix(p1, p2)
        return result['rows'][0]['elements'][0]['distance']['value']
