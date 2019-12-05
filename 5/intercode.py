import os, copy
from functools import reduce
import operator

def read_code():
    file = os.path.dirname(os.path.abspath(__file__)) + '/data/input'
    with open(file) as fh:
        intercode = [int(x) for x in fh.read().split(',')]
    return intercode

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

def get_values(parameterModes, instructions, intercode):
    values = []
    for instruction in instructions:
        if parameterModes:
            parameter = parameterModes.pop(0)
            if parameter == 0:
                values.append(intercode[instruction])
            elif parameter == 1:
                values.append(instruction)
        else:
            values.append(intercode[instruction])
    return values


def run_intercode(intercode, input_value):
    instructionPointer = 0
    output = None
    while instructionPointer <= len(intercode):
        opcode, modeParameters = get_opcode_and_parameters(intercode[instructionPointer])
        print("OPCODE: {}".format(opcode))
        print("parameters: {}".format(modeParameters))

        if opcode == 99:
            return output

        if opcode == 1:
            inputParameters = intercode[instructionPointer+1:instructionPointer+3]
            values = get_values(modeParameters, inputParameters, intercode)
            outputParameter = intercode[instructionPointer+3]
            intercode[outputParameter] = sum(values)
            instructionPointer += 4
        elif opcode == 2:
            inputParameters = intercode[instructionPointer+1:instructionPointer+3]
            values = get_values(modeParameters, inputParameters, intercode)
            outputParameter = intercode[instructionPointer+3]
            intercode[outputParameter] = reduce(operator.mul, values)
            instructionPointer += 4
        elif opcode == 3:
            inputParameter1 = intercode[instructionPointer+1]
            intercode[inputParameter1] = input_value
            instructionPointer += 2
        elif opcode == 4:
            inputParameters = [intercode[instructionPointer+1]]
            values = get_values(modeParameters, inputParameters, intercode)
            output = values[0]
            instructionPointer += 2
        elif opcode == 5:
            inputParameters = \
                intercode[instructionPointer+1:instructionPointer+3]
            values = get_values(modeParameters, inputParameters, intercode)
            if values[0] != 0:
                instructionPointer = values[1]
            else:
                instructionPointer += 3
        elif opcode == 6:
            inputParameters = \
                intercode[instructionPointer+1:instructionPointer+3]
            values = get_values(modeParameters, inputParameters, intercode)
            if values[0] == 0:
                instructionPointer = values[1]
            else:
                instructionPointer += 3
        elif opcode == 7:
            inputParameters = \
                intercode[instructionPointer+1:instructionPointer+3]
            values = get_values(modeParameters, inputParameters, intercode)
            outputParameter = intercode[instructionPointer+3]
            if values[0] < values[1]:
                intercode[outputParameter] = 1
            else:
                intercode[outputParameter] = 0
            instructionPointer += 4
        elif opcode == 8:
            inputParameters = \
                intercode[instructionPointer+1:instructionPointer+3]
            values = get_values(modeParameters, inputParameters, intercode)
            outputParameter = intercode[instructionPointer+3]
            if values[0] == values[1]:
                intercode[outputParameter] = 1
            else:
                intercode[outputParameter] = 0
            instructionPointer += 4
        else:
            print("SOMETHING WENT WRONG")
            return
    return output



def main():
    # intercode = [1, 0, 0, 0, 99]
    # intercode = [1,1,1,4,99,5,6,0,99]
    # memory = copy.copy(intercode)
    # intercode[1] = 12
    # intercode[2] = 2

    # intercode = [3,0,4,0,99]
    intercode = read_code()
    # intercode = [3,9,8,9,10,9,4,9,99,-1,8]
    # intercode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    # intercode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,\
    #              1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104, \
    #              999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    input_value = 5

    return run_intercode(intercode, input_value)

if __name__ == "__main__":
    print(main())
