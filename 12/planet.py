"""
Planet class
"""


class Planet():

    """Planet"""

    def __init__(self, position, planet_system):
        """
        :planet_position: [x,y,z]
        :planet_system: PlanetSystem

        """
        self.pos = position
        self.v = 0
        self.planet_system = planet_system
        self.visited = []
        self.v_visited = []

    def visit(self):
        self.visited.append(self.pos)
        self.v_visited.append(self.v)

    def is_repeating(self):
        if len(self.visited) > 20:
            return self.visited[-10:] == self.visited[:10] and \
                self.v_visited[-10:] == self.v_visited[:10]
        else:
            return False

        # s = self.velocity_visiteds[axis]
        # i = (s+s).find(s[:100000], 1, -1)
        # if i != -1:
        #     self.found_repetitions[1][axis] = s[:i]


    def set_velocity(self):
        """
        TODO
        """
        for planet in set(self.planet_system.planets) - set([self]):
            if planet.pos > self.pos:
                self.v += 1
            elif planet.pos < self.pos:
                self.v -= 1

    def move(self):
        """
        TODO
        """
        self.pos += self.v

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
