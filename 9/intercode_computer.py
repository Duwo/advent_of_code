import os, copy
from amplifier import Amplifier

class IntercodeComputer():
    def __init__(self, intercode, amp_mode, feedback_mode):
        self.intercode = intercode
        self.amplifiers = []
        self.amp_mode = amp_mode
        self.feedback_mode = feedback_mode
        self.output = ''

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
                    self.output += str(amp.output) + ','
        return done

    def calculate(self, input_value=None):
        done = False
        while not done:
            done = self.amplify_signal(input_value)
            if self.feedback_mode:
                input_value = self.output

