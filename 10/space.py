"""
Space class
"""
from asteroid import Asteroid


class Space():
    """
    TODO
    """
    def __init__(self, space_rows):
        self.space_rows = space_rows
        self.asteroids = []

    def create_asteroids(self):
        """
        TODO
        """
        coordinates = self.parse_positions()
        for coord in coordinates:
            self.asteroids.append(
                Asteroid(coord)
            )

    def parse_positions(self):
        """
        TODO
        """
        coordinates = []
        for _y, row in enumerate(self.space_rows):
            for _x, column in enumerate(row):
                if column == '#':
                    coordinates.append((_x, _y))

        return coordinates





