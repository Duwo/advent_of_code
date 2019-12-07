import os


NODES = []

class Node:
    def __init__(self, val, next_val):
        self.val = val
        self.next_val = next_val
        self.next = None # the pointer initially points to nothing

    def traverse_to(self, val):
        node = self # start from the head node
        orbits = []
        while node.next_val != val:
            node = node.next
            orbits.append(node.next_val)

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
        orbits += len(node.traverse_to('COM'))

    return orbits

def find_common_ancestor(my_orbits, santa_orbits):
    common_ansecstor = my_orbits.pop(0)
    while common_ansecstor not in santa_orbits:
        common_ansecstor = my_orbits.pop(0)

    return common_ansecstor

def main():
    read_nodes()
    sort_nodes()
    me =find_node('YOU')
    santa = find_node('SAN')
    my_orbits = me.traverse_to('COM')
    santa_orbits = santa.traverse_to('COM')
    common_ansecstor = find_common_ancestor(my_orbits, santa_orbits)
    orbital_transfers = len(me.traverse_to(common_ansecstor)) + len(santa.traverse_to(common_ansecstor))
    print(orbital_transfers)


if __name__ == "__main__":
    main()
