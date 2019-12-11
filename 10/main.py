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

    best_observer = Observer(None, space)
    for asteroid in space.asteroids:
        observer = Observer(asteroid, space)
        observer.caclulate_visable_asteroids()
        if len(observer.asteroid_sight_vectors) > \
                len(best_observer.asteroid_sight_vectors):
            best_observer = observer

    hello_sorted = best_observer.order_sight_vectors_for_laser()
    coords = hello_sorted[199][1].coords
    print(coords[0]*100 + coords[1])
    # while best_observer.destroyed_asteroids != 200:
    #     asteroid = best_observer.shot_laser()

    # print(len(best_observer.asteroid_sight_vectors))


if __name__ == "__main__":
    main()
