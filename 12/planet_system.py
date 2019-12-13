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
            planet.visit()

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

    def calculate_repetitions(self):
        for planet in self.planets:
            position_frequencies = planet.get_frequencies()
            print(position_frequencies)
            break

    def calculate_steps(self):
        x_position_repetition = self.claculate_x_repetition()
        # y_position_repetition = self.claculate_x_repetition()
        # z_position_repetition = self.claculate_x_repetition()

        # x_velocity_repetition = self.claculate_x_repetition()
        # y_velocity_repetition = self.claculate_x_repetition()
        # z_velocity_repetition = self.claculate_x_repetition()






