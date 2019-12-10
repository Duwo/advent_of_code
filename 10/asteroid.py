"""
Asteroid class
"""


class Asteroid():
    def __init__(self, coords):
        self.coords = coords

    def distance(self, asteroid):
        """
        TODO
        """
        distance = \
            abs(self.coords[0] - asteroid.coords[0]) + \
            abs(self.coords[1] - asteroid.coords[1])
        return distance
