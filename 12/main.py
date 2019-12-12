"""
run Solarsystem
"""
import os, re
from planet import Planet
from planet_system import PlanetSystem


def read_planet_positions():
    file = os.path.dirname(os.path.abspath(__file__)) + '/data/input'
    with open(file) as fh:
        planet_strings = fh.read().splitlines()

    planets = []
    for planet_string in planet_strings:
        m = re.findall(r'(-?\d+)', planet_string)
        planets.append([int(m[0]),int(m[1]),int(m[2])])
    return planets


def main():
    """
    TODO
    """
    planet_positions = read_planet_positions()
    planet_system = PlanetSystem()
    for position in planet_positions:
        planet_system.planets.append(Planet(position, planet_system))

    for _i in range(1000):
        planet_system.step()
        # for planet in planet_system.planets:
            # print(planet.position)

    print(planet_system.get_energy())

if __name__ == "__main__":
    main()
