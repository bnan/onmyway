import json

class CircuitsResource:
    def __init__(self):
        pass

    def on_get(self, request, response):
        circuit = {
            'foo': 5,
            'bar': 7
        }

        resp.body = json.dumps(circuit)
