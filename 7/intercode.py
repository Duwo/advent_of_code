import os, copy
from functools import reduce
import operator
from itertools import permutations

class Amplifier():
    def __init__(self, phase_setting, intercode):
        self.phase_setting = phase_setting
        self.instruction_pointer = 0
        self.first_input =  True
        self.output_address = None
        self.use_phase_setting = True
        self.memory = copy.copy(intercode)

    def get_opcode_and_parameters(self):
        instructions = str(self.memory[self.instruction_pointer])
        try:
            opcode = int(instructions[-2:])
            parameters = list(instructions[:-2])
        except:
            return int(instructions), []

        parameter_list = []
        while parameters:
            parameter_list.append(int(parameters.pop()))
        return opcode, parameter_list

    def get_values(self, parameter_modes, instructions):
        values = []
        for instruction in instructions:
            if parameter_modes:
                parameter = parameter_modes.pop(0)
                if parameter == 0:
                    values.append(self.memory[instruction])
                elif parameter == 1:
                    values.append(instruction)
            else:
                values.append(self.memory[instruction])
        return values

    def handle_one(self, mode_parameters):
        input_parameters = \
            self.memory[self.instruction_pointer+1:self.instruction_pointer+3]
        values = self.get_values(mode_parameters, input_parameters)
        output_parameter = self.memory[self.instruction_pointer+3]
        self.memory[output_parameter] = sum(values)
        self.instruction_pointer += 4

    def handle_two(self, mode_parameters):
        input_parameters = \
            self.memory[self.instruction_pointer+1:self.instruction_pointer+3]
        values = self.get_values(mode_parameters, input_parameters)
        output_parameter = self.memory[self.instruction_pointer+3]
        self.memory[output_parameter] = reduce(operator.mul, values)
        self.instruction_pointer += 4

    def handle_three(self, mode_parameters, input_signal):
        input_parameter = self.memory[self.instruction_pointer+1]
        if self.use_phase_setting and self.first_input:
            self.memory[input_parameter] = self.phase_setting
            self.first_input = False
        else:
            self.memory[input_parameter] = input_signal
        self.instruction_pointer += 2

    def handle_four(self, mode_parameters):
        self.output_address = self.memory[self.instruction_pointer+1]
        self.instruction_pointer += 2

    def handle_five(self, mode_parameters):
        input_parameters = \
            self.memory[self.instruction_pointer+1:self.instruction_pointer+3]
        values = self.get_values(mode_parameters, input_parameters)
        if values[0] != 0:
            self.instruction_pointer = values[1]
        else:
            self.instruction_pointer += 3

    def handle_six(self, mode_parameters):
        input_parameters = \
            self.memory[self.instruction_pointer+1:self.instruction_pointer+3]
        values = self.get_values(mode_parameters, input_parameters)
        if values[0] == 0:
            self.instruction_pointer = values[1]
        else:
            self.instruction_pointer += 3

    def handle_seven(self, mode_parameters):
        input_parameters = \
            self.memory[self.instruction_pointer+1:self.instruction_pointer+3]
        values = self.get_values(mode_parameters, input_parameters)
        output_parameter = self.memory[self.instruction_pointer+3]
        if values[0] < values[1]:
            self.memory[output_parameter] = 1
        else:
            self.memory[output_parameter] = 0

        self.instruction_pointer += 4

    def handle_eight(self, mode_parameters):
        input_parameters = \
            self.memory[self.instruction_pointer+1:self.instruction_pointer+3]
        values = self.get_values(mode_parameters, input_parameters)
        output_parameter = self.memory[self.instruction_pointer+3]
        if values[0] == values[1]:
            self.memory[output_parameter] = 1
        else:
            self.memory[output_parameter] = 0

        self.instruction_pointer += 4

    def run_code(self, input_signal):
        while self.instruction_pointer <= len(self.memory):
            opcode, mode_parameters = self.get_opcode_and_parameters()
            # print("Opcode: {}".format(opcode))
            # print("parameters: {}".format(mode_parameters))

            if opcode == 99:
                done = True
                output = self.memory[self.output_address]
                return output, done

            if opcode == 1:
                self.handle_one(mode_parameters)
            elif opcode == 2:
                self.handle_two(mode_parameters)
            elif opcode == 3:
                self.handle_three(mode_parameters, input_signal)
            elif opcode == 4:
                self.handle_four(mode_parameters)
                done = False
                output = self.memory[self.output_address]
                print('Sending signal output: ', output)
                return output, done
            elif opcode == 5:
                self.handle_five(mode_parameters)
            elif opcode == 6:
                self.handle_six(mode_parameters)
            elif opcode == 7:
                self.handle_seven(mode_parameters)
            elif opcode == 8:
                self.handle_eight(mode_parameters)
            else:
                print("SOMETHING WENT WRONG")
                return

class IntercodeComputer():
    def __init__(self, setting_combination, intercode):
        self.amplifiers = self.create_amplifiers(setting_combination, intercode)
        self.feedback_mode = True

    def create_amplifiers(self, setting_combination, intercode):
        amplifiers = []
        for phase_setting in setting_combination:
            amplifiers.append(Amplifier(phase_setting, intercode))

        return amplifiers

    def amplify_signal(self, input_signal):
        for amp in self.amplifiers:
            print('Sending signal to amp: ', input_signal)
            output, done = amp.run_code(input_signal)
            print('Got signal from amp: ', output)
            input_signal = copy.copy(output)
        return output, done

    def calculate(self):
        current, done = self.amplify_signal(0)
        if self.feedback_mode:
            done = False
            while not done:
                print('----------------------')
                print('Starting feedback with: ', current)
                current, done = self.amplify_signal(current)
                print('Is done: ', done)

        return current


def read_code():
    file = os.path.dirname(os.path.abspath(__file__)) + '/data/input'
    intercode = []
    with open(file) as fh:
        for x in fh.read().split(','):
            intercode.append(int(x))
    return intercode

def main():
    intercode = read_code()
    # phase_list = [[1,0,4,3,2]]

    # phase_list = [[9,8,7,6,5]]
    # intercode = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    # phase_list = [[9,7,8,5,6]]
    # intercode = \
    #     [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,\
    #      -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,\
    #      53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    # return
    # phase_list = [[4,3,2,1,0]]
    # intercode = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    # phase_list = [[0,1,2,3,4]]
    # intercode = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
    #              101,5,23,23,1,24,23,23,4,23,99,0,0]
    # phase_list = [[1,0,4,3,2]]
    # intercode = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33, \
    #              1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    # phase_list = [[1,0,4,3,2]]
    # intercode = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,\
    #              1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

    phase_list = permutations([5,6,7,8,9], 5)
    # phase_list = permutations([0,1,2,3,4], 5)
    outputs = []
    for setting_combination in phase_list:
        computer = IntercodeComputer(setting_combination, intercode)
        computer.feedback_mode = True
        outputs.append(computer.calculate())

    print(max(outputs))


if __name__ == "__main__":
    main()
