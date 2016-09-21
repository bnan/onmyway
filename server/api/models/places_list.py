class PlacesList(list):
    def tripify(self, current_location):
        """Sorts the list in place according to the distance relative to each place in it, so that each walk from one
        place to another is hopefully minimal

        Keyword arguments:
        current_location -- first location to compare to
        """
        i = 0
        while i < len(self):
            current_location = min(self[i:], key=current_location.distance)
            self.swap(i, self.index(current_location))
            i += 1

    # Swaps two elements of the list
    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]

    def __dict__(self):
        return [place.__dict__() for place in self]
