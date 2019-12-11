import os, copy
from amplifier import Amplifier

class IntercodeComputer():
    def __init__(self, intercode, amp_mode, feedback_mode):
        self.intercode = intercode
        self.amplifiers = []
        self.amp_mode = amp_mode
        self.feedback_mode = feedback_mode
        self.output = ''
        self.grid = [['.']*1000 for i in range(1000)]
        self.current_position = [500,500]
        self.painted_positions = []
        # 0 = right, 1 = up, 2 = left, 3 = down
        self.direction = 1
        self.should_move = False
        self.nr_painted = 0

    def create_amplifiers(self, setting_combination=[]):
        if self.amp_mode:
            for phase_setting in setting_combination:
                self.amplifiers.append(Amplifier(phase_setting, self.intercode, self))
        else:
            self.amplifiers.append(Amplifier([], self.intercode, self))

    def reset_memory(self, setting_combination=[]):
        self.amplifiers = []

    def amplify_signal(self, input_signal):
        for amp in self.amplifiers:
            done = False
            while not done:
                done = amp.run_code(input_signal)
                if self.amp_mode:
                    input_signal = amp.output
                    self.output = amp.ouput
                elif not done:
                    if self.should_move:
                        self.move(amp.output)
                        self.should_move = False
                        if self.position_is_white():
                            input_signal = 1
                        else:
                            input_signal = 0
                    else:
                        if not self.position_already_painted():
                            self.nr_painted += 1
                        self.paint(amp.output)
                        self.should_move = True

        return done

    def paint(self, instruction):
        if instruction == 1:
            if self.position_already_painted():
                self.grid[self.current_position[1]][self.current_position[0]] = '#'
            else:
                self.grid[self.current_position[1]][self.current_position[0]] = '#'
                self.painted_positions.append(copy.copy(self.current_position))
        elif instruction == 0:
            if self.position_already_painted():
                self.grid[self.current_position[1]][self.current_position[0]] = '.'
            else:
                self.grid[self.current_position[1]][self.current_position[0]] = '.'
                self.painted_positions.append(copy.copy(self.current_position))


    def move(self, instruction):
        if instruction == 0:
            self.turn_left()
            self.step()
        elif instruction == 1:
            self.turn_right()
            self.step()

    def turn_left(self):
        if self.direction == 3:
            self.direction = 0
        else:
            self.direction += 1

    def turn_right(self):
        if self.direction == 0:
            self.direction = 3
        else:
            self.direction -= 1

    def step(self):
        if self.direction == 0:
            self.current_position[0] += 1
        elif self.direction == 1:
            self.current_position[1] += 1
        elif self.direction == 2:
            self.current_position[0] -= 1
        elif self.direction == 3:
            self.current_position[1] -= 1

    def position_is_black(self):
        return \
            self.grid[self.current_position[1]][self.current_position[0]] == '.'

    def position_is_white(self):
        return \
            self.grid[self.current_position[1]][self.current_position[0]] == '#'

    def position_already_painted(self):
        return self.current_position in self.painted_positions

    def calculate(self, input_value=None):
        done = False
        while not done:
            done = self.amplify_signal(input_value)
            print("only once")
            break
            if self.feedback_mode:
                input_value = self.output

