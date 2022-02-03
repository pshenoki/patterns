class House:
    def __init__(self, maket):
        self.maket = maket

    def view(self):
        for level_name, level in self.maket.items():
            print(level_name + ':' + level)


class CubeHouseBuilder:
    def __init__(self, maket):
        self.maket = maket
        self.plan = House(maket)

    def make_level_1(self):
        if 'level_1' in self.maket:
            self.maket['level_1'] = '|---------|'
        return self

    def make_level_2(self):
        if 'level_2' in self.maket:
            self.maket['level_2'] = '|         |'
        return self

    def make_level_3(self):
        if 'level_3' in self.maket:
            self.maket['level_3'] = '| |Х| |Х| |'
        return self

    def make_level_4(self):
        if 'level_4' in self.maket:
            self.maket['level_4'] = '|_________|'
        return self

    def create(self):
        return self.plan


class MushroomHouseBuilder:
    def __init__(self, maket):
        self.maket = maket
        self.plan = House(maket)

    def make_level_1(self):
        if 'level_1' in self.maket:
            self.maket['level_1'] = ' |-------|'
        return self

    def make_level_2(self):
        if 'level_2' in self.maket:
            self.maket['level_2'] = ' |__   __|'
        return self

    def make_level_3(self):
        if 'level_3' in self.maket:
            self.maket['level_3'] = '   |  |'
        return self

    def make_level_4(self):
        if 'level_4' in self.maket:
            self.maket['level_4'] = '   |__|'
        return self

    def create(self):
        return self.plan


class Director:

    @staticmethod
    def create_building(builder, maket):
        return builder(maket)\
            .make_level_1()\
            .make_level_2()\
            .make_level_3()\
            .make_level_4()\
            .create()


if __name__ == '__main__':
    maket_1 = {'level_1': '', 'level_2': '', 'level_3': '', 'level_4': ''}
    maket_2 = {'level_1': '', 'level_3': '', 'level_4': ''}

    cube_house = Director.create_building(CubeHouseBuilder, maket_1)
    cube_house.view()
    print('')

    cube_house = Director.create_building(CubeHouseBuilder, maket_2)
    cube_house.view()
    print('')

    mushroom_house = Director.create_building(MushroomHouseBuilder, maket_1)
    mushroom_house.view()



