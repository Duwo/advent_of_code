"""
Factory class
"""
import copy


class Factory():
    def __init__(self):
        self.reactions = {}
        self.stored_materials = { 'ORE': 0 }
        self.used_ore = 0
        self.cargo_ore = 1000000000000

    def get_material(self, material, amount):
        self.reactions[material][0].get_material(amount)

    def dissemble_to_ore(self):
        for key in self.stored_materials.keys():
            amount = self.stored_materials[key]
            if key != 'ORE' and self.stored_materials[key] > 0:
                self.reactions[key][0].dissemble_material(amount)

    def reset(self):
        for key in self.stored_materials.keys():
            self.stored_materials[key] = 0
        # self.cargo_ore = 13312
        self.cargo_ore = 1000000000000
        # self.cargo_ore = 13312

    def produce_from_cargo(self, material):
        self.get_material('FUEL', 1)
        one_time_ore = copy.copy(self.used_ore)
        one_time_leftovers = copy.copy(self.stored_materials)
        self.reset()

        # print(one_time_ore)
        # print(one_time_leftovers)
        iterations = 0
        while self.cargo_ore >= one_time_ore:
            full_fuel_prod_times = int(self.cargo_ore / one_time_ore)
            iterations += full_fuel_prod_times
            self.cargo_ore -= full_fuel_prod_times * one_time_ore
            for key in one_time_leftovers.keys():
                if key != 'ORE':
                    self.stored_materials[key] += \
                        one_time_leftovers[key] * full_fuel_prod_times

            self.dissemble_to_ore()
            # full_fuel_prod_times = int(self.cargo_ore / one_time_ore)
        print(iterations)
        print(self.stored_materials)

        return iterations
