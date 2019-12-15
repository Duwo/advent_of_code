import os


def read_reactions():
    file = os.path.dirname(os.path.abspath(__file__)) + '/data/input'
    reactions = []
    with open(file) as fh:
        reaction_strings = fh.read().splitlines()

    for reaction_string in reaction_strings:
        reaction = reaction_string.split('=>')
        output = reaction[1].strip().split(' ')
        reaction_output = {
            'name': output[1].strip(),
            'quantity': output[0].strip()
        }
        inputs = reaction[0].strip().split(',')
        reaction_inputs = []
        for reaction_input in inputs:
            reaction_input = reaction_input.strip().split(' ')
            reaction_inputs.append(
                {
                    'name': reaction_input[1].strip(),
                    'quantity': reaction_input[0].strip()
                }
            )
        reactions.append(
            {
                'inputs': reaction_inputs,
                'output': reaction_output
            }
        )

    return reactions


from factory import Factory
from reaction import Reaction


if __name__ == "__main__":
    parsed_reactions = read_reactions()
    factory = Factory()
    ore_reaction = Reaction('ORE', 1, factory, dependencies = [])
    factory.reactions['ORE'] = (ore_reaction, 1)
    reactions = Reaction.create_from_dict(parsed_reactions, factory)
    factory.get_material('FUEL', 1)
    # full_fuel_prod = int(factory.cargo_ore / factory.used_ore)
    print(factory.used_ore)
    # print(factory.produce_from_cargo('FUEL'))










