import os, copy
import random
from amplifier import Amplifier

class IntercodeComputer():
    def __init__(self, intercode, amp_mode, feedback_mode):
        self.intercode = intercode
        self.code_runners = []
        self.output = ''
        self.grid = [[' ']*100 for i in range(100)]
        self.position = [50, 50]
        self.explored_walls = []
        self.explored_empty = []
        self.target = [38, 68]
        self.steps = 0


    def create_droid(self):
        self.code_runners.append(Amplifier([], self.intercode, self))
        self.grid[self.position[1]][self.position[0]] = 'S'

    def reset_memory(self, setting_combination=[]):
        self.amplifiers = []

    def run(self, input_signal):
        done = False
        amp = self.code_runners[0]
        while not done:
            amp.run_code(input_signal)
            done, input_signal = self.handle_status_code(input_signal, amp.output)
        # while not done:
        #     amp.run_code(input_signal)
        #     done, input_signal = self.handle_status_code(input_signal,
        #                                                  amp.output
        #                                                  target)

        return done

    def next_position(self, input_signal):
        if input_signal == 1:
            return [self.position[0], self.position[1] + 1]
        elif input_signal == 2:
            return [self.position[0], self.position[1] - 1]
        elif input_signal == 3:
            return [self.position[0] - 1, self.position[1]]
        elif input_signal == 4:
            return [self.position[0] + 1, self.position[1]]

    def next_movement(self):
        possible_nexts = \
            [self.next_position(1),
             self.next_position(2),
             self.next_position(3),
             self.next_position(4)]
        directions = [i for i in range(4)]

        for i, next_pos in enumerate(possible_nexts):
            if next_pos in self.explored_walls:
                directions.remove(i)

        backtrack = []
        for i, next_pos in enumerate(possible_nexts):
            if next_pos in self.explored_empty:
                directions.remove(i)
                backtrack.append(i)

        possible_nexts_no_walls = [possible_nexts[i] for i in directions]
        possible_backtracks_no_walls = [possible_nexts[i] for i in backtrack]

        if directions:
            # if self.target:
            #     best_next = self.get_minimum_to_target(possible_nexts_no_walls)
            #     self.steps += 1
                # return possible_nexts.index(best_next) + 1
            direction = random.randint(0, len(directions)-1)
            self.steps += 1
            return directions[direction] + 1
        else:
            # if self.target:
            #     best_next = self.get_minimum_to_target(possible_backtracks_no_walls)
            #     self.steps += 1
            #     return possible_nexts.index(best_next) + 1
            direction = random.randint(0, len(backtrack)-1)
            self.steps -= 1
            return backtrack[direction] + 1

    def get_minimum_to_target(self, next_positions):
        sorted_nexts = sorted(
            next_positions,
            key=lambda pos: abs(pos[0]-self.target[0]) + abs(pos[1] - self.target[1])
        )
        return sorted_nexts[0]

    def handle_status_code(self, input_signal, output):
        next_position = copy.copy(self.next_position(input_signal))
        done = False
        if output == 0:
            self.grid[next_position[1]][next_position[0]] = '#'
            self.explored_walls.append(next_position)
            input_signal = self.next_movement()
        elif output == 1:
            self.grid[next_position[1]][next_position[0]] = '.'
            self.explored_empty.append(next_position)
            self.position = next_position
            input_signal = self.next_movement()
        elif output == 2:
            self.grid[next_position[1]][next_position[0]] = 'O'
            print('Found oxygen at: ', next_position)
            done = True
            input_signal = None

        return done, input_signal



