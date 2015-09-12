from api.clients.googlemaps_client import GoogleMapsClient

google_client = GoogleMapsClient()


class Place(object):
    def __init__(self, name, lat, lng, icon, hours):
        self.name = name
        self.lat = float(lat)
        self.lng = float(lng)
        self.icon = icon
        self.hours = hours

    def __dict__(self):
        return {
            'name': self.name,
            'icon': self.icon,
            'hours': self.hours,
            'location': {
                'lat': self.lat,
                'lng': self.lng
            }
        }

    def get_name(self):
        return self.name

    def get_lat(self):
        return self.lat

    def get_lng(self):
        return self.lng

    def set_name(self, name):
        self.name = name

    def set_lat(self, lat):
        self.lat = float(lat)

    def set_lng(self, lng):
        self.lng = float(lng)

    def distance(self, p2):
        lat1, lng1 = self.lat, self.lng
        lat2, lng2 = p2.get_lat(), p2.get_lng()
        return google_client.distance_between((lat1, lng1), (lat2, lng2))
