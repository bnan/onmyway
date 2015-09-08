import json
from api.circuits.circuits_foursquare import CircuitsFoursquare
from api.circuits.util.PlacesList import PlacesList

class CircuitsResource:
    def on_get(self, request, response, location = 'Porto', number_of_places = 5, interests = ['coffee']):
        circuits_foursquare = CircuitsFoursquare()

        results = circuits_foursquare.search(location, number_of_places, interests)

        result = PlacesList()

        for venue in results['venues']:
            result.extend([{
                'location': venue['location'],
                'name': venue['name']
            }])


        # TODO: pass the list of places through the algorithm to generate a circuit
        circuits = result

        response.body = json.dumps(circuits)
