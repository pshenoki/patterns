""" Паттерн:
        Строитель (Builder)
    Суть паттерна:
        Паттерн "Строитель" позволяет создавать сложные объекты пошагово.
        Строитель даёт возможность использовать один и тот же код строительства
        для получения разных представлений объектов.
    Задача:
        1. Создать класс Дом, который бы имел план строительства.
        2. Создать класс Строитель, который бы строил дом по макету, но в своем стиле. """


class House:
    def __init__(self, maket):
        self.maket = maket

    def view(self):
        for level_name, level in self.maket.items():
            print(level_name + ':' + level)


class CubeHouseBuilder:
    """ Строитель в кубическом стиле """
    def __init__(self, maket):
        self.maket = maket
        self.house = House(maket)

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
        return self.house


class MushroomHouseBuilder:
    """ Строитель в грибном стиле """
    def __init__(self, maket):
        self.maket = maket
        self.house = House(maket)

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
        return self.house


class Director:
    """ Класс директор, который принимает макет дома и строителя и строит обьект
        (не имеет особо отношения к паттерну, создан для красоты)"""
    @staticmethod
    def create_building(builder, maket):
        return builder(maket)\
            .make_level_1()\
            .make_level_2()\
            .make_level_3()\
            .make_level_4()\
            .create()


if __name__ == '__main__':
    # Пусть есть два макета дома
    maket_1 = {'level_1': '', 'level_2': '', 'level_3': '', 'level_4': ''}
    maket_2 = {'level_1': '', 'level_3': '', 'level_4': ''}

    # Построим дом по чертежу №1 с помощью кубического строителя и грибного.
    cube_house = Director.create_building(CubeHouseBuilder, maket_1)
    cube_house.view()
    print('.' * 40)
    mushroom_house = Director.create_building(MushroomHouseBuilder, maket_1)
    mushroom_house.view()
    print('.' * 40)

    # Построим дом по чертежу №2 с помощью кубического строителя и грибного.
    cube_house = Director.create_building(CubeHouseBuilder, maket_2)
    cube_house.view()
    print('.' * 40)
    mushroom_house = Director.create_building(MushroomHouseBuilder, maket_2)
    mushroom_house.view()

