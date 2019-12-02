import os

def read_code():
    file = os.path.dirname(os.path.abspath(__file__)) + '/data/input'
    with open(file) as fh:
        intercode = [int(x) for x in fh.read().split(',')]
    return intercode


def main():
    # intercode = [1, 0, 0, 0, 99]
    # intercode = [1,1,1,4,99,5,6,0,99]
    intercode = read_code()
    print(intercode)
    print("-----------------")
    intercode[1] = 12
    intercode[2] = 2
    length = len(intercode)

    for i in range(length):
        if not (i == 0 or i % 4 == 0):
            continue

        if intercode[i] == 99:
            return intercode

        optcode = intercode[i]
        inputPosition1 = intercode[i+1]
        inputPosition2 = intercode[i+2]
        outputPosition = intercode[i+3]

        if optcode == 1:
            try :
                intercode[outputPosition] = intercode[inputPosition1] + intercode[inputPosition2]
            except:
                pass
        elif optcode == 2:
            try:
                intercode[outputPosition] = intercode[inputPosition1] * intercode[inputPosition2]
            except:
                pass

    return intercode

if __name__ == "__main__":
    print(main())
