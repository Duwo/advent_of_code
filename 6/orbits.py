import os


NODES = []

class Node:
    def __init__(self, val, next_val):
        self.val = val
        self.next_val = next_val
        self.next = None # the pointer initially points to nothing

    def traverse(self):
        node = self # start from the head node
        orbits = 0
        while node.next_val != 'COM':
            node = node.next # move on to the next node
            orbits += 1
        orbits += 1
        return orbits

def read_nodes():
    file = os.path.dirname(os.path.abspath(__file__)) + '/data/input'
    with open(file) as fh:
        lines = fh.read().splitlines()[:-1]
        for line in lines:
            orbit, val = line.split(')')
            NODES.append(Node(val, orbit))

def sort_nodes():
    for node in NODES:
        node.next = find_node(node.next_val)


def find_node(val):
    for node in NODES:
        if node.val == val:
            return node

def count_orbits():
    orbits = 0
    for node in NODES:
        orbits += node.traverse()

    return orbits

def main():
    read_nodes()
    sort_nodes()
    orbits = count_orbits()
    print(orbits)


if __name__ == "__main__":
    main()
