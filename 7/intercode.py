import os, copy
from functools import reduce
import operator
from itertools import permutations

INTERCODE = []
INTERCODE_MEMORY = []

def read_code():
    global INTERCODE
    global INTERCODE_MEMORY
    file = os.path.dirname(os.path.abspath(__file__)) + '/data/input'
    INTERCODE = []
    with open(file) as fh:
        for x in fh.read().split(','):
            INTERCODE.append(int(x))
    INTERCODE_MEMORY = copy.copy(INTERCODE)

def get_opcode_and_parameters(number):
    numbers = str(number)
    try:
        opcode = int(numbers[-2:])
        parameters = list(numbers[:-2])
    except:
        return number, []

    parameter_list = []
    while parameters:
        parameter_list.append(int(parameters.pop()))
    return opcode, parameter_list

def get_values(parameterModes, instructions):
    global INTERCODE
    values = []
    for instruction in instructions:
        if parameterModes:
            parameter = parameterModes.pop(0)
            if parameter == 0:
                values.append(INTERCODE[instruction])
            elif parameter == 1:
                values.append(instruction)
        else:
            values.append(INTERCODE[instruction])
    return values

def run_intercode(input_instructions):
    global INTERCODE
    instructionPointer = 0
    output = None
    while instructionPointer <= len(INTERCODE):
        intstruction = INTERCODE[instructionPointer]
        opcode, modeParameters = get_opcode_and_parameters(intstruction)
        # print("OPCODE: {}".format(opcode))
        # print("parameters: {}".format(modeParameters))

        if opcode == 99:
            return output

        if opcode == 1:
            inputParameters = INTERCODE[instructionPointer+1:instructionPointer+3]
            values = get_values(modeParameters, inputParameters)
            outputParameter = INTERCODE[instructionPointer+3]
            INTERCODE[outputParameter] = sum(values)
            instructionPointer += 4
        elif opcode == 2:
            inputParameters = INTERCODE[instructionPointer+1:instructionPointer+3]
            values = get_values(modeParameters, inputParameters)
            outputParameter = INTERCODE[instructionPointer+3]
            INTERCODE[outputParameter] = reduce(operator.mul, values)
            instructionPointer += 4
        elif opcode == 3:
            inputParameter1 = INTERCODE[instructionPointer+1]
            inputParameter2 = INTERCODE[instructionPointer+1]
            INTERCODE[inputParameter1] = input_instructions.pop(0)
            instructionPointer += 2
        elif opcode == 4:
            inputParameters = [INTERCODE[instructionPointer+1]]
            values = get_values(modeParameters, inputParameters)
            output = values[0]
            instructionPointer += 2
        elif opcode == 5:
            inputParameters = \
                INTERCODE[instructionPointer+1:instructionPointer+3]
            values = get_values(modeParameters, inputParameters)
            if values[0] != 0:
                instructionPointer = values[1]
            else:
                instructionPointer += 3
        elif opcode == 6:
            inputParameters = \
                INTERCODE[instructionPointer+1:instructionPointer+3]
            values = get_values(modeParameters, inputParameters)
            if values[0] == 0:
                instructionPointer = values[1]
            else:
                instructionPointer += 3
        elif opcode == 7:
            inputParameters = \
                INTERCODE[instructionPointer+1:instructionPointer+3]
            values = get_values(modeParameters, inputParameters)
            outputParameter = INTERCODE[instructionPointer+3]
            if values[0] < values[1]:
                INTERCODE[outputParameter] = 1
            else:
                INTERCODE[outputParameter] = 0
            instructionPointer += 4
        elif opcode == 8:
            inputParameters = \
                INTERCODE[instructionPointer+1:instructionPointer+3]
            values = get_values(modeParameters, inputParameters)
            outputParameter = INTERCODE[instructionPointer+3]
            if values[0] == values[1]:
                INTERCODE[outputParameter] = 1
            else:
                INTERCODE[outputParameter] = 0
            instructionPointer += 4
        else:
            print("SOMETHING WENT WRONG")
            return
    return output


def main():
    global INTERCODE
    global INTERCODE_MEMORY
    read_code()
    outputs = []
    for setting_combination in permutations([0,1,2,3,4], 5):
        input_signal = 0
        for phase_setting in setting_combination:
            input_instructions = [phase_setting, input_signal]
            INTERCODE = copy.copy(INTERCODE_MEMORY)
            input_signal = run_intercode(input_instructions)
        outputs.append(input_signal)

    print(max(outputs))

if __name__ == "__main__":
    main()
