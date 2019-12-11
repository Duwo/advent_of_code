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
    input_value = 0
    amp_mode = False
    feedback_mode = False
    computer = IntercodeComputer(intercode, amp_mode, feedback_mode)
    if amp_mode:
        for setting_combination in phase_list:
            computer.create_amplifiers(setting_combination)
            outputs.append(computer.calculate(0))
            computer.reset_memory(setting_combination)
    else:
        computer.create_amplifiers(0)
        computer.calculate(input_value)
        print(computer.nr_painted)

if __name__ == "__main__":
    main()
