"""
Observer class
"""
from fractions import Fraction
from operator import itemgetter


class Observer():
    def __init__(self, asteroid, space):
        self.asteroid = asteroid
        self.space = space
        self.asteroid_sight_vectors = []
        self.destroyed_asteroids = 0

    def caclulate_visable_asteroids(self):
        asteroids_by_distance = sorted(
            self.space.asteroids,
            key=lambda asteroid: asteroid.distance(self.asteroid)
        )

        # remove self
        for asteroid in asteroids_by_distance[1:]:
            sight_vector = self.sight_vector(asteroid)
            if self.asteroid_is_visible(sight_vector):
                self.asteroid_sight_vectors.append((sight_vector, asteroid))

    def asteroid_is_visible(self, sight_vector):
        current_sight_vectors = [asteroid_sight_vector[0] for asteroid_sight_vector in
                                 self.asteroid_sight_vectors]
        return sight_vector not in current_sight_vectors

    def sight_vector(self, asteroid):
        d_y = asteroid.coords[1] - self.asteroid.coords[1]
        d_x = asteroid.coords[0] - self.asteroid.coords[0]

        if d_x == 0:
            vector = (d_x, int(d_y/abs(d_y)))
        elif d_y == 0:
            vector = (int(d_x/abs(d_x)), d_y)
        else:
            frac = Fraction(d_x, d_y)
            y = abs(frac.denominator)/(d_y/abs(d_y))
            x = abs(frac.numerator)/(d_x/abs(d_x))
            vector = (x, y)

        return vector

    def order_sight_vectors_for_laser(self):
        right_side = []
        for ast_sight in self.asteroid_sight_vectors:
            if ast_sight[0][0] == 0 and ast_sight[0][1] > 0:
                saved_zero = ast_sight
            if ast_sight[0][0] > 0:
                right_side.append(ast_sight)

        sorted_right = sorted(
            right_side,
            key=lambda ast_sight: ast_sight[0][1]/ast_sight[0][0],
            reverse=True
        )
        sorted_right.insert(0, saved_zero)

        left_side = []
        for ast_sight in self.asteroid_sight_vectors:
            if ast_sight[0][0] == 0 and ast_sight[0][1] < 0:
                saved_zero = ast_sight
            if ast_sight[0][0] < 0:
                left_side.append(ast_sight)

        sorted_left = sorted(
            left_side,
            key=lambda ast_sight: -ast_sight[0][1]/ast_sight[0][0],
            reverse=True
        )
        sorted_left.insert(0, saved_zero)

        return sorted_right + sorted_left

    def shot_laser(self):
        pass


