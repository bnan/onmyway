class PlacesList(list):
    #   Sorts the list in place according to the distance relative to each place in the list (so that each walk from one
    # place to another is hopefully minimal)
    #####
    # TODO: Method (p1 = Place()).distTo(Place p2) is not yet implemented!
    #####
    def order(self, current_location):
        i = 0
        while i < len(self):
            current_location = min(self[i:], key=current_location.distTo)
            self.swap(i, self.index(current_location))
            i += 1

    # Swaps two elements of the list
    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]
