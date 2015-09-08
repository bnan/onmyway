from api.circuits.circuits_model import CircuitsModel


class CircuitsRepository:
    def __init__(self):
        self.circuit_model = CircuitsModel()

    def get_by_id(self, id):
        pass
        # get circuit using the circuit model

    def create(self, circuit):
        pass
        # create circuit using the circuit model
