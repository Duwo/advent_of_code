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
            print(values)
            print(outputParameter)
            intercode[outputParameter] = reduce(operator.mul, values)
            instructionPointer += 4
        elif opcode == 3:
            inputParameter1 = intercode[instructionPointer+1]
            intercode[inputParameter1] = input_value
            instructionPointer += 2
        elif opcode == 4:
            inputParameter1 = intercode[instructionPointer+1]
            output = intercode[inputParameter1]
            print('new output check')
            print(output)
            instructionPointer += 2
        else:
            print("SOMTHING WENT WRONG")
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
    # intercode = [1002,4,3,4,33]
    input_value = 1

    return run_intercode(intercode, input_value)


    # return run_intercode(intercode)
    # for i in range(1, 100):
    #     intercode[1] = i
    #     for j in range(1, 100):
    #         intercode[2] = j
    #         if run_intercode(intercode)[0] == 19690720:
    #             return 100*i + j
    #         else:
    #             intercode = copy.copy(memory)
    #             intercode[1] = i

if __name__ == "__main__":
    print(main())
