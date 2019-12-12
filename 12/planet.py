"""
Planet class
"""


class Planet():

    """Planet"""

    def __init__(self, planet_position, planet_system):
        """
        :planet_position: [x,y,z]
        :planet_system: PlanetSystem

        """
        self.position = planet_position
        self.velocity = [0,0,0]
        self.planet_system = planet_system

    def set_velocity(self):
        """
        TODO
        """
        for planet in set(self.planet_system.planets) - set([self]):
            for axis in range(3):
                if planet.position[axis] > self.position[axis]:
                    self.velocity[axis] += 1
                elif planet.position[axis] < self.position[axis]:
                    self.velocity[axis] -= 1

    def move(self):
        """
        TODO
        """
        for axis in range(3):
            self.position[axis] += self.velocity[axis]

    def potential_energy(self):
        energy = 0
        for axis in range(3):
            energy += abs(self.position[axis])
        return energy

    def kinetic_energy(self):
        energy = 0
        for axis in range(3):
            energy += abs(self.velocity[axis])
        return energy

    def get_energy(self):
        """
        TODO
        """
        return self.potential_energy() * self.kinetic_energy()

        return energy

