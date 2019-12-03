import os


def main():
    # wire_input = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'], ['U62','R66','U55','R34','D71','R55','D58','R83']
    # wire1, wire2 = ['R8','U5','L5','D3'], ['U7','R6','D4','L4']
    wire1, wire2 = read_wires()
    coords_wire1 = convert_to_coords(wire1)
    coords_wire2 = convert_to_coords(wire2)
    wire_crossings = set(coords_wire1).intersection(set(coords_wire2))
    steps_to_crossings = find_steps_to_crossings(wire1, wire2, wire_crossings)
    manhattan_min_crossing = manhattan_min(wire_crossings)
    steps_min = manhattan_min(steps_to_crossings)

    return steps_min #manhattan_min_crossing

def find_steps_to_crossings(wire1, wire2, crossings):
    steps = []
    for crossing in crossings:
        steps.append((wire_steps_to_crossing(wire1, crossing),
                     wire_steps_to_crossing(wire2, crossing)))

    return steps

def wire_steps_to_crossing(wire, crossing):
    total_steps = 0
    current_position = (0, 0)
    for step in wire:
        direction = step[0]
        length = int(step[1:]) + 1
        if direction == 'R':
            for i in range(1, length):
                total_steps += 1
                current_position = (current_position[0]+1, current_position[1])
                if current_position == crossing:
                    return total_steps
        if direction == 'L':
            for i in range(1, int(length)):
                total_steps += 1
                current_position = (current_position[0]-1, current_position[1])
                if current_position == crossing:
                    return total_steps
        if direction == 'D':
            for i in range(1, int(length)):
                total_steps += 1
                current_position = (current_position[0], current_position[1]-1)
                if current_position == crossing:
                    return total_steps
        if direction == 'U':
            for i in range(1, int(length)):
                total_steps += 1
                current_position = (current_position[0], current_position[1]+1)
                if current_position == crossing:
                    return total_steps

def read_wires():
    file = os.path.dirname(os.path.abspath(__file__)) + '/data/input'
    with open(file) as fh:
        wires = fh.read().splitlines()

    wire_input = [wire.split(',') for wire in wires]
    return wire_input

def manhattan_min(wire_crossings):
    distances = []
    for crossing in wire_crossings:
        distances.append(sum([abs(crossing[0]), abs(crossing[1])]))

    return min(distances)


def convert_to_coords(wire):
    coords = []
    current_position = (0, 0)
    for step in wire:
        direction = step[0]
        length = int(step[1:]) + 1
        if direction == 'R':
            for i in range(1, length):
                coords.append((current_position[0]+i, current_position[1]))
        if direction == 'L':
            for i in range(1, int(length)):
                coords.append((current_position[0]-i, current_position[1]))
        if direction == 'D':
            for i in range(1, int(length)):
                coords.append((current_position[0], current_position[1]-i))
        if direction == 'U':
            for i in range(1, int(length)):
                coords.append((current_position[0], current_position[1]+i))
        current_position = coords[-1]

    return coords

if __name__ == "__main__":
    print(main())
