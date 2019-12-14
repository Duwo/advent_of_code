import os, copy
from amplifier import Amplifier

class IntercodeComputer():
    def __init__(self, intercode, amp_mode, feedback_mode):
        self.intercode = intercode
        self.amplifiers = []
        self.amp_mode = amp_mode
        self.feedback_mode = feedback_mode
        self.output = ''
        self.grid = [[0]*100 for i in range(20)]
        self.nr_block_tiles = 0
        self.position = []
        self.tile_type = None

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
                self.handle_output(amp.output)

        return done

    def handle_output(self, output):
        if len(self.position) < 2:
            self.position.append(output)
            return

        self.handle_tile_type(output)
        self.position = []

    def handle_tile_type(self, output):
        if output == 2:
            self.nr_block_tiles += 1

    def calculate(self, input_value=None):
        done = False
        while not done:
            done = self.amplify_signal(input_value)
            print("only once")
            break
            if self.feedback_mode:
                input_value = self.output

