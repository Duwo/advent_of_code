"""
PlanetSystem class
"""


class PlanetSystem():

    """PlanetSystem"""

    def __init__(self):
        """TODO: """
        self.planets = []

    def step(self):
        """
        TODO
        """
        for planet in self.planets:
            planet.set_velocity()

        for planet in self.planets:
            planet.move()

    def get_energy(self):
        """
        TODO
        """
        energy = 0
        for planet in self.planets:
            energy += planet.get_energy()

        return energy





