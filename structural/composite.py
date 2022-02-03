class Component:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_full_price(self):
        print(f"{self.name} - {self.price}")
        return self.price


class Box(Component):
    def __init__(self):
        self.items = set()

    def add_item(self, components):
        for component in components:
            self.items.add(component)

    def remove_item(self, component):
        self.items.remove(component)

    def get_full_price(self):
        price = 0
        for component in self.items:
            price += component.get_full_price()
        return price


com1 = Component('pen', 11)
com2 = Component('pencil', 12)
box = Box()
box.add_item([com1, com2])
print(box.get_full_price())
print('------------------------------')
com3 = Component('rubber', 13)
multi_box = Box()
multi_box.add_item([box, com3])
print(multi_box.get_full_price())
print('------------------------------')
multi_pulti_box = Box()
multi_pulti_box.add_item([multi_box, box])
print(multi_pulti_box.get_full_price())

