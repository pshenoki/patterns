""" Паттерн:
        Легковес (Flyweight)
    Суть паттерна:
        Паттерн "Легковес" позволяет вместить бóльшее количество объектов в отведённую оперативную память.
        Легковес экономит память, разделяя общее состояние объектов между собой,
        вместо хранения одинаковых данных в каждом объекте.
    Задача:
        1. Создать класс Зомби с изменяющимися параметрами и нет.
        2. Создать класс Легковес, который бы создавал зомби и хранил только уникальных зомби в памяти,
           а также хранил неизменяемые параметры в себе. """


class SimpleZombie:
    def __init__(self, hp, damage, sex, lvl):
        self.hp = hp
        self.damage = damage
        self.sex = sex
        self.lvl = lvl
        self.type_ = 'simple'
        self.items = 'stone'


class SimpleZombieFlyweight:
    def __init__(self):
        self.type_ = 'simple'
        self.items = 'stone'
        self.zombie_list = []

    def simple_zombie_factory(self, hp, damage, sex, lvl):
        for zomb in self.zombie_list:
            if (zomb.hp, zomb.damage, zomb.sex, zomb.lvl) == (hp, damage, sex, lvl):
                return zomb

        self.zombie_list.append(SimpleZombie(hp, damage, sex, lvl))
        return SimpleZombie(hp, damage, sex, lvl)

    def get_info(self):
        for zomb in self.zombie_list:
            print("zombie (hp: {}, dmg: {}, sex: {}, lvl: {}, type: {}, weapon: {}),"
                  .format(zomb.hp, zomb.damage, zomb.sex, zomb.lvl, self.type_, self.items))


if __name__ == '__main__':
    # Создадим армию зомби
    zombie_army = SimpleZombieFlyweight()

    # C разными параметрами:
    zombie_army.simple_zombie_factory(100, 10, 'male', 1)
    zombie_army.simple_zombie_factory(100, 10, 'male', 2)
    zombie_army.simple_zombie_factory(100, 10, 'male', 3)

    # И с одинаковыми параметрами:
    zombie_army.simple_zombie_factory(100, 10, 'female', 1)
    zombie_army.simple_zombie_factory(100, 10, 'female', 1)
    zombie_army.simple_zombie_factory(100, 10, 'female', 1)

    # Посмотрим, что получилось
    zombie_army.get_info()

    """ Смысл в том, что имея большую армию одинаковых зомби,
        мы можем не хранить в памати все состояния этих зомби,
        а хранить только уникальных."""