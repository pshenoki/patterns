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
    zombie = SimpleZombieFlyweight()
    zombie.simple_zombie_factory(100, 10, 'male', 1)
    zombie.simple_zombie_factory(100, 10, 'male', 2)
    zombie.simple_zombie_factory(100, 10, 'male', 3)

    zombie.simple_zombie_factory(100, 10, 'female', 1)
    zombie.simple_zombie_factory(100, 10, 'female', 1)
    zombie.simple_zombie_factory(100, 10, 'female', 1)

    zombie.get_info()
