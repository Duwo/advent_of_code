"""
Reaction class
"""


class Reaction():
    def __init__(self, name, quantity, factory, dependencies=[]):
        self.name = name
        self.quantity = quantity
        self.factory = factory
        self.dependencies = dependencies
        self.from_ore = 0

    def get_dependencies(self):
        if self.name == 'ORE':
            return None
        else:
            return self.dependencies

    @classmethod
    def create_from_dict(cls, parsed_reactions, factory):
        """TODO

        :parsed_reactions: TODO
        :returns: reactions dict

        """
        reactions = []
        while len(factory.reactions) < len(parsed_reactions) + 1:
            for parsed_reaction in parsed_reactions:
                dependencies = []
                dependency_fail = False
                for dependency in parsed_reaction['inputs']:
                    try:
                        amount = int(dependency['quantity'])
                        dependency = factory.reactions[dependency['name']][0]
                        dependencies.append((dependency, amount))
                    except KeyError:
                        dependency_fail = True
                        break
                if not dependency_fail:
                    reaction = Reaction(
                        parsed_reaction['output']['name'],
                        int(parsed_reaction['output']['quantity']),
                        factory,
                        dependencies
                    )
                    factory.reactions[reaction.name] = \
                        (reaction,
                         int(parsed_reaction['output']['quantity']))

    def get_material(self, amount):
        while self.storage_amount() < amount:
            self.produce()

        self.get_from_storage(amount)


    def produce(self):
        if self.name == 'ORE':
            self.factory.used_ore += self.quantity
            self.factory.cargo_ore -= self.quantity
        else:
            for dependency in self.dependencies:
                dependency[0].get_material(dependency[1])

        self.save_to_storage(self.quantity)

    def dissemble_material(self, amount):
        dissemble_iterations = int(amount/self.quantity)

        if self.name == 'ORE':
            self.factory.cargo_ore += amount
        elif dissemble_iterations >= 1:
            for dependency in self.dependencies:
                    dependency_conversion_quantity = \
                        dependency[1] * dissemble_iterations
                    dependency[0].save_to_storage(
                        dependency_conversion_quantity
                    )
                    dependency[0].dissemble_material(
                        dependency_conversion_quantity
                    )

            self.remove_from_storage(
                self.quantity * dissemble_iterations
            )

    def remove_from_storage(self, amount):
        self.factory.stored_materials[self.name] -= amount

    def storage_amount(self):
        try:
            return self.factory.stored_materials[self.name]
        except KeyError:
            return 0

    def save_to_storage(self, amount):
        try:
            self.factory.stored_materials[self.name] += amount
        except KeyError:
            self.factory.stored_materials[self.name] = amount

    def get_from_storage(self, amount):
        self.factory.stored_materials[self.name] -= amount


