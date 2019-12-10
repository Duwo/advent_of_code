"""
Space Observer
"""
import os
from space import Space
from observer import Observer


def read_space():
    """
    TODO
    """
    file = os.path.dirname(os.path.abspath(__file__)) + '/data/input'
    space_rows = []
    with open(file) as fh:
        for row in fh.read().splitlines():
            space_rows.append(row)

    # return ['#.', '#.']
    return space_rows


def main():
    """
    TODO
    """
    space_rows = read_space()
    space = Space(space_rows)
    space.create_asteroids()

    visable_asteroids = []
    for asteroid in space.asteroids:
        observer = Observer(asteroid, space)
        observer.caclulate_visable_asteroids()
        visable_asteroids.append(len(observer.asteroid_sight_vectors))

    print(max(visable_asteroids))


if __name__ == "__main__":
    main()
