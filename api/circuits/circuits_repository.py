import json
from circuits.circuits_model import CircuitsModel

class CircuitsRepository:
    def __init__(self):
        self.circuit_model = CircuitsModel()

    def get_by_id(self, id):
        # get circuit using the circuit model

    def create(self, circuit):
        # create circuit using the circuit model
