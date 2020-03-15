import math
import os


def fuel_module(module_mass):
    fuel_sum = 0
    if module_mass:
        module_mass = int(module_mass)
        fuel_mass = fuel_calc(module_mass)
        while fuel_mass > 0:
            fuel_sum += fuel_mass
            fuel_mass = fuel_calc(fuel_mass)
        return fuel_sum
    else:
        return 0


def fuel_calc(mass):
    return math.floor(mass / 3) - 2


def fuel_modules(lines):
    sum = 0
    for module_mass in lines:
        sum += fuel_module(module_mass)
    return sum


def fuel_file(file):
    with open(file) as fh:
        lines = fh.read().splitlines()
        fuel = fuel_modules(lines)

    return fuel


if __name__ == '__main__':
    examples = [12, 14, 1969, 100756]

    for module_mass in examples:
        print(fuel_module(module_mass))

    file = os.path.dirname(os.path.abspath(__file__)) + '/data/input'
    print(fuel_file(file))
