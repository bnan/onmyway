import json
from api.circuits.circuits_foursquare import CircuitsFoursquare


class CircuitsResource:
    def on_get(self, request, response, location = 'Porto', number_of_places = 5, interests = []):
        circuits_foursquare = CircuitsFoursquare()

        results = circuits_foursquare.search(location, number_of_places, interests)

        # TODO: pass the list of places through the algorithm to generate a circuit
        circuits = results

        response.body = json.dumps(circuits)
