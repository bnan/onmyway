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
            current_location = self.min2(self[i:])
            self.swap(i, self.index(current_location))
            i += 1

    # Swaps two elements of the list
    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]

    def min2(self, current_location):
        r, i, min_r = 0, 0, maxsize
        while i < len(self):
            dist = distance(current_location, self[i])
            if dist < min_r:
                min_r = dist
                r = i
            i += 1
        return self[i]


def distance(v1, v2):
    lat1, lng1 = v1['location']['lat'], v1['location']['lng']
    lat2, lng2 = v2['location']['lat'], v2['location']['lng']
    return GoogleMapsClient().distance_between((lat1, lng1), (lat2, lng2))
