from api.clients.googlemaps_client import GoogleMapsClient


class Place(dict):
    def distance_to(self, p):
        return GoogleMapsClient().distance_between(self, p)
