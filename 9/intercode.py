import os
from itertools import permutations
from intercode_computer import IntercodeComputer

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

    input_value= None
    # intercode = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

    input_value = 2
    # intercode = [1102,34915192,34915192,7,4,7,99,0]
    # intercode = [104,1125899906842624,99]
    # intercode = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

    amp_mode = False
    feedback_mode = False
    outputs = []
    computer = IntercodeComputer(intercode, amp_mode, feedback_mode)
    # phase_list = permutations([5,6,7,8,9], 5)
    # phase_list = permutations([0,1,2,3,4], 5)
    if amp_mode:
        for setting_combination in phase_list:
            computer.create_amplifiers(setting_combination)
            outputs.append(computer.calculate(0))
            computer.reset_memory(setting_combination)
    else:
        computer.create_amplifiers()
        computer.calculate(input_value)
        print(computer.output)

    return

    # print(max(outputs))


if __name__ == "__main__":
    main()
