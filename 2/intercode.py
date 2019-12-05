import os, copy

def read_code():
    file = os.path.dirname(os.path.abspath(__file__)) + '/data/input'
    with open(file) as fh:
        intercode = [int(x) for x in fh.read().split(',')]
    return intercode


def run_intercode(intercode):
    length = len(intercode)
    for instructionPointer in range(length):
        if not (instructionPointer == 0 or instructionPointer % 4 == 0):
            continue

        if intercode[instructionPointer] == 99:
            return intercode

        optcode = intercode[instructionPointer]
        inputParameter1 = intercode[instructionPointer+1]
        inputParameter2 = intercode[instructionPointer+2]
        outputParameter = intercode[instructionPointer+3]

        if optcode == 1:
            intercode[outputParameter] = intercode[inputParameter1] + intercode[inputParameter2]
        elif optcode == 2:
            intercode[outputParameter] = intercode[inputParameter1] * intercode[inputParameter2]

    return intercode



def main():
    # intercode = [1, 0, 0, 0, 99]
    # intercode = [1,1,1,4,99,5,6,0,99]
    intercode = read_code()
    memory = copy.copy(intercode)
    intercode[1] = 12
    intercode[2] = 2

    # return run_intercode(intercode)
    for i in range(1, 100):
        intercode[1] = i
        for j in range(1, 100):
            intercode[2] = j
            if run_intercode(intercode)[0] == 19690720:
                return 100*i + j
            else:
                intercode = copy.copy(memory)
                intercode[1] = i

if __name__ == "__main__":
    print(main())
