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
    input_value = 1
    amp_mode = False
    feedback_mode = False
    droid = IntercodeComputer(intercode, amp_mode, feedback_mode)
    if amp_mode:
        for setting_combination in phase_list:
            computer.create_amplifiers(setting_combination)
            outputs.append(computer.calculate(0))
            computer.reset_memory(setting_combination)
    else:
        droid.create_droid()
        droid.run(input_value)
        file = os.path.dirname(os.path.abspath(__file__)) + '/data/output'
        with open(file, 'w+') as fh:
            for row in droid.grid:
                fh.write(''.join(row) + '\n')

if __name__ == "__main__":
    main()
