from api.clients.googlemaps_client import GoogleMapsClient
from sys import maxsize


class PlacesList(list):
    def order(self, current_location):
        """Sorts the list in place according to the distance relative to each place in it (so that each walk from one
        place to another is hopefully minimal)

        Keyword arguments:
        current_location -- first location to compare to
        """
        # TODO: Method (p1 = Place()).distTo(Place p2) is not yet implemented!
        i = 0
        while i < len(self):
            # current_location = min(self[i:], key=current_location.distance_to)
            current_location = min2(self[i:], current_location)
            self.swap(i, self.index(current_location))
            i += 1

    # Swaps two elements of the list
    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]


def min2(places, current_location):
    r, i, min_dist = 0, 0, maxsize
    while i < len(places):
        dist = distance(current_location, places[i])
        if dist < min_dist:
            min_dist = dist
            r = i
        i += 1
    return places[r]


def distance(v1, v2):
    lat1, lng1 = v1['location']['lat'], v1['location']['lng']
    lat2, lng2 = v2['location']['lat'], v2['location']['lng']
    return GoogleMapsClient().distance_between((lat1, lng1), (lat2, lng2))
