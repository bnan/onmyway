import falcon
from api.http.circuits_resource import CircuitsResource

router = falcon.API()

circuits = CircuitsResource()

router.add_route('/circuits/{location}/{interests}/{number_of_places}', circuits)
