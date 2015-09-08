from api.clients.googlemaps_client import GoogleMapsClient


class Place(dict):
    def distance_to(self, p):
        lat1, lng1 = self['location']['lat'], self['location']['lng']
        lat2, lng2 = p['location']['lat'], p['location']['lng']
        return GoogleMapsClient().distance_between((lat1, lng1), (lat2, lng2))
