import copy
from functools import reduce
import operator


class Amplifier():
    def __init__(self, phase_setting, intercode, computer):
        self.phase_setting = phase_setting
        self.instruction_pointer = 0
        self.first_input =  True
        self.output_address = None
        self.use_phase_setting = False
        self.computer = computer
        self.memory = copy.copy(intercode) + 10000000*[0]
        self.relative_base = 0
        self.output = None

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
                elif parameter == 2:
                    values.append(self.memory[instruction +
                                              self.relative_base])
            else:
                values.append(self.memory[instruction])


        return values

    def get_output_address(self, mode_parameters, relative_instruction):
        if mode_parameters:
            mode = mode_parameters.pop()
            if mode == 1:
                address = self.instruction_pointer+relative_instruction
            elif mode == 2:
                address = self.relative_base + \
                    self.memory[self.instruction_pointer+relative_instruction]
        else:
            address = self.memory[self.instruction_pointer+relative_instruction]

        return address


    def handle_one(self, mode_parameters):
        input_parameters = \
            self.memory[self.instruction_pointer+1:self.instruction_pointer+3]
        values = self.get_values(mode_parameters, input_parameters)
        output_address = self.get_output_address(mode_parameters, 3)
        self.memory[output_address] = sum(values)
        self.instruction_pointer += 4

    def handle_two(self, mode_parameters):
        input_parameters = \
            self.memory[self.instruction_pointer+1:self.instruction_pointer+3]
        values = self.get_values(mode_parameters, input_parameters)
        output_address = self.get_output_address(mode_parameters, 3)
        self.memory[output_address] = reduce(operator.mul, values)
        self.instruction_pointer += 4

    def handle_three(self, mode_parameters, input_signal):
        input_parameter = self.memory[self.instruction_pointer+1]
        if self.use_phase_setting and self.first_input:
            self.memory[input_parameter] = self.phase_setting
            self.first_input = False
            self.instruction_pointer += 2
            return

        address = self.get_output_address(mode_parameters, 1)
        self.memory[address] = input_signal
        self.instruction_pointer += 2

    def handle_four(self, mode_parameters):
        self.output_address = self.get_output_address(mode_parameters, 1)
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
        output_parameter = self.get_output_address(mode_parameters, 3)
        if values[0] < values[1]:
            self.memory[output_parameter] = 1
        else:
            self.memory[output_parameter] = 0

        self.instruction_pointer += 4

    def handle_eight(self, mode_parameters):
        input_parameters = \
            self.memory[self.instruction_pointer+1:self.instruction_pointer+3]
        values = self.get_values(mode_parameters, input_parameters)
        output_address = self.get_output_address(mode_parameters, 3)
        if values[0] == values[1]:
            self.memory[output_address] = 1
        else:
            self.memory[output_address] = 0

        self.instruction_pointer += 4

    def handle_nine(self, mode_parameters):
        address = self.get_output_address(mode_parameters, 1)
        value = self.memory[address]
        self.relative_base += value
        # print(value)
        # print("Relative_base: ", self.relative_base)
        self.instruction_pointer += 2

    def run_code(self, input_signal):
        while self.instruction_pointer <= len(self.memory):
            opcode, mode_parameters = self.get_opcode_and_parameters()
            # print("Opcode: {}".format(opcode))
            # print("parameters: {}".format(mode_parameters))

            if opcode == 99:
                done = True
                self.output = self.memory[self.output_address]
                return done

            if opcode == 1:
                self.handle_one(mode_parameters)
            elif opcode == 2:
                self.handle_two(mode_parameters)
            elif opcode == 3:
                self.handle_three(mode_parameters, input_signal)
            elif opcode == 4:
                self.handle_four(mode_parameters)
                done = False
                self.output = self.memory[self.output_address]
                return done
            elif opcode == 5:
                self.handle_five(mode_parameters)
            elif opcode == 6:
                self.handle_six(mode_parameters)
            elif opcode == 7:
                self.handle_seven(mode_parameters)
            elif opcode == 8:
                self.handle_eight(mode_parameters)
            elif opcode == 9:
                self.handle_nine(mode_parameters)
            else:
                return True
                print("SOMETHING WENT WRONG")
                return
