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

    # return [[-1,0,2], [2,-10,-7], [4,-8,8], [3,5,-1]]
    return planets
    # return [[1], [-1]]

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

from functools import reduce
import operator
import re


def main():
    """
    TODO
    """
    planet_positions = read_planet_positions()
    planet_system = PlanetSystem()
    for position in planet_positions:
        planet_system.planets.append(Planet(position, planet_system))

    for _i in range(1000000):
        planet_system.step()

    for planet in planet_system.planets:
        planet.get_frequencies()

        # print(planet_system.get_energy())


    planet_repetitions = []
    for planet in planet_system.planets:
        for repetition in planet.found_repetitions[0]:
            planet_repetitions.append(len(repetition.split(',')[:-1]))

        for repetition in planet.found_repetitions[1]:
            planet_repetitions.append(len(repetition.split(',')[:-1]))

    # flat_list = [item for sublist in planet_repetitions for item in sublist]
    # flat_list = [item for sublist in flat_list for item in sublist]
    # print(flat_list)
    primes = []
    for number in planet_repetitions:
        new_primes = prime_factors(number)
        for prime in new_primes:
            if prime not in primes:
                primes.append(prime)
            if new_primes.count(prime) > primes.count(prime):
                primes.append(prime)

    print(reduce(operator.mul, primes))


def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

if __name__ == "__main__":
    main()
