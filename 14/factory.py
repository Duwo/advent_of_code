"""
Factory class
"""
import copy
import math


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
        self.stored_materials['ORE'] = 1000000000000

        # self.cargo_ore = 13312

    def produce_from_cargo(self, material):
        self.get_material('FUEL', 1)
        one_time_ore = copy.copy(self.used_ore)
        one_time_leftovers = copy.copy(self.stored_materials)
        self.reset()
        iterations = 0
        numbers = []
        while self.cargo_ore >= one_time_ore:
            full_fuel_prod_times = int(self.cargo_ore / one_time_ore)
            iterations += full_fuel_prod_times
            self.cargo_ore -= full_fuel_prod_times * one_time_ore
            self.stored_materials['ORE'] -= full_fuel_prod_times * one_time_ore
            for key in one_time_leftovers.keys():
                if key != 'ORE':
                    self.stored_materials[key] += \
                        one_time_leftovers[key] * full_fuel_prod_times
            self.dissemble_to_ore()
            self.dissemble_to_ore()
            self.dissemble_to_ore()

        while self.cargo_ore > 0:
            self.get_material('FUEL', 1)
            iterations += 1
            self.dissemble_to_ore()

        print(self.cargo_ore)
        print(self.stored_materials)

        print(iterations)

        return iterations
