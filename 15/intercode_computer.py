import os, copy
import random
from amplifier import Amplifier


class IntercodeComputer():
    def __init__(self, intercode, amp_mode, feedback_mode):
        self.intercode = intercode
        self.code_runners = None
        self.oxygen = None
        self.grid = [[' ']*100 for i in range(100)]
        self.position = [50, 50]
        self.possible_positions = [[[50,50]]]
        self.target = [38, 68]
        self.steps = 1
        self.current_depth = 0


    def create_droid(self):
        self.code_runner = Amplifier([], self.intercode, self)
        self.grid[self.position[1]][self.position[0]] = 'S'

    def run(self, input_signal):
        steps = 1
        while not self.oxygen:
            current_path = [copy.copy(self.position)]
            self.explore(current_path)
            self.steps += 1

        return self.steps

    def explore(self, current_path):
        if len(current_path) == self.steps:
            self.explore_new()
        else:
            print(self.possible_positions)
            for position in self.possible_positions[self.steps-1]:
                self.code_runner.run_code(position[0])
                self.position = position[1]
                current_path.append(position)
                self.explore(current_path)
                position =  current_path.pop()
                self.code_runner.run_code(self.revert_input(position[0]))
                self.position = position[1]


    def explore_new(self):
        input_signals = [signal for signal in range(1,5)]
        for input_signal in input_signals:
            self.code_runner.run_code(input_signal)
            self.handle_status_code(self.code_runner.output, input_signal)

    def next_position(self, input_signal):
        if input_signal == 1:
            return (1, [self.position[0], self.position[1] + 1])
        elif input_signal == 2:
            return (2,[self.position[0], self.position[1] - 1])
        elif input_signal == 3:
            return (3, [self.position[0] - 1, self.position[1]])
        elif input_signal == 4:
            return (4, [self.position[0] + 1, self.position[1]])

    def revert_input(self, input_signal):
        if input_signal == 1:
            return 2
        elif input_signal == 2:
            return 1
        elif input_signal == 3:
            return 4
        elif input_signal == 4:
            return 3

    def add_to_positions(self, next_position):
        if len(self.possible_positions) < self.steps + 1:
            self.possible_positions.append([])

        if self.already_added(next_position) or self.going_back(next_position):
            pass
        else:
            self.possible_positions[self.steps].append(next_position)

    def already_added(self, next_position):
        return next_position in self.possible_positions[self.steps]

    def going_back(self, next_position):
        if len(self.possible_positions) < 3:
            return False
        return next_position in self.possible_positions[self.steps - 2]

    def handle_wall(self, next_position):
        self.grid[next_position[1][1]][next_position[1][0]] = '#'

    def handle_empty(self, next_position, input_signal):
        self.grid[next_position[1][1]][next_position[1][0]] = '.'
        self.add_to_positions(next_position)

    def hanlde_oxygen_tank(self, next_position):
        self.grid[next_position[1][1]][next_position[1][0]] = 'O'
        self.oxygen = next_position

    def handle_status_code(self, output, input_signal):
        next_position = self.next_position(input_signal)
        if output == 0:
            self.handle_wall(next_position)
        elif output == 1:
            self.handle_empty(next_position, input_signal)
        elif output == 2:
            self.handle_oxygen_tanke(next_position)

