import os, copy
from amplifier import Amplifier

class IntercodeComputer():
    def __init__(self, intercode, amp_mode, feedback_mode):
        self.intercode = intercode
        self.amplifiers = []
        self.amp_mode = amp_mode
        self.feedback_mode = feedback_mode
        self.output = ''
        self.grid = [['.']*40 for i in range(40)]
        self.nr_block_tiles = 0
        self.position = []
        self.ball_x = None
        self.paddle_x = None
        self.ball_dx = None


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
                input_signal = self.move_paddle()
                done = amp.run_code(input_signal)
                self.handle_output(amp.output)

        return done

    def move_paddle(self):
        if self.paddle_x and self.ball_x and self.ball_dx:
            if self.paddle_x < self.ball_x:
                input_signal = 1
            elif self.paddle_x > self.ball_x:
                input_signal = -1
            else:
                input_signal = 0
        else:
            input_signal = 0

        return input_signal

    def handle_output(self, output):
        if len(self.position) < 2:
            self.position.append(output)
            return

        if self.position == [-1,0]:
            print('Score: ', output)
        self.handle_tile_type(output)
        self.position = []

    def handle_tile_type(self, output):
        if output == 0:
            pass
        elif output == 1:
            self.grid[self.position[1]][self.position[0]] = '|'
        elif output == 2:
            self.grid[self.position[1]][self.position[0]] = '#'
            self.nr_block_tiles += 1
        elif output == 3:
            self.grid[self.position[1]][self.position[0]] = 'P'
            self.paddle_x = self.position[0]
        elif output == 4:
            self.grid[self.position[1]][self.position[0]] = 'O'
            self.ball_x = self.position[0]

    def calculate(self, input_value=None):
        done = False
        while not done:
            done = self.amplify_signal(input_value)
            print("only once")
            break
            if self.feedback_mode:
                input_value = self.output

