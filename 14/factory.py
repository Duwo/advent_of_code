"""
Factory class
"""
import copy


class Factory():
    def __init__(self):
        self.reactions = {}
        self.stored_materials = {}
        self.used_ore = 0
        self.cargo_ore =  1000000000000

    def get_material(self, material, amount):
        self.reactions[material][0].get_material(amount)

    def produce_from_cargo(self, material):
        self.get_material('FUEL', 1)
        one_time_ore = copy.copy(self.used_ore)
        full_fuel_prod_times = int(self.cargo_ore /self.used_ore)
        for key in self.stored_materials.keys():
            self.stored_materials[key] *= full_fuel_prod_times
        self.cargo_ore -= full_fuel_prod_times * self.used_ore

        while self.used_ore == one_time_ore:
            self.get_material(100)
            full_fuel_prod_times += 100
