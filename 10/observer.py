"""
Observer class
"""
from fractions import Fraction


class Observer():
    def __init__(self, asteroid, space):
        self.asteroid = asteroid
        self.space = space
        self.asteroid_sight_vectors = []

    def caclulate_visable_asteroids(self):
        asteroids_by_distance = sorted(
            self.space.asteroids,
            key=lambda asteroid: asteroid.distance(self.asteroid)
        )

        # remove self
        for asteroid in asteroids_by_distance[1:]:
            asteroid_sight_vector = self.sight_vector(asteroid)
            if self.asteroid_is_visible(asteroid_sight_vector):
                self.asteroid_sight_vectors.append(asteroid_sight_vector)
        # if self.asteroid.coords == (5,8):
        #     __import__('pdb').set_trace()

    def asteroid_is_visible(self, sight_vector):
        return sight_vector not in self.asteroid_sight_vectors

    def sight_vector(self, asteroid):
        d_y = asteroid.coords[1] - self.asteroid.coords[1]
        d_x = asteroid.coords[0] - self.asteroid.coords[0]

        if d_x == 0:
            vector = (d_x, int(d_y/abs(d_y)))
        elif d_y == 0:
            vector = (int(d_x/abs(d_x)), d_y)
        elif 1 in [abs(d_y), abs(d_x)]:
            vector = (d_x, d_y)
        else:
            frac = Fraction(d_x, d_y)
            y = abs(frac.denominator)/(d_y/abs(d_y))
            x = abs(frac.numerator)/(d_x/abs(d_x))
            vector = (x, y)

        return vector
