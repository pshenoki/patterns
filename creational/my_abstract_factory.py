""" Паттерн:
        Абстрактная фабрика (Abstract factory)
    Суть паттерна:
        Паттерн "Фабричный метод" позволяет создавать семейства связанных объектов,
        не привязываясь к конкретным классам создаваемых объектов.
    Задача:
        1. Создать класс Абстрактная Фабрика, который бы создавал фабрики определенного года.
        2. Создать класс Фабрика, который бы создавал модели определенного года."""

from abc import abstractmethod, ABC


class Transport(ABC):

    @abstractmethod
    def run(self):
        pass


class Plane1990(Transport):

    def run(self):
        return 'plane 1990 run'


class Auto1990(Transport):

    def run(self):
        return 'auto 1990 run'


class Plane2000(Transport):

    def run(self):
        return 'plane 2000 run'


class Auto2000(Transport):

    def run(self):
        return 'auto 2000 run'


class AbsFactory(ABC):
    """ Абстрактная фабрика будет создавать фабрики по производству в зависимости от года """
    @staticmethod
    def create_factory(model):

        models = {
            1990: Factory1990(),
            2000: Factory2000()
        }
        return models[model]

    @abstractmethod
    def create_auto(self):
        pass

    @abstractmethod
    def create_plan(self):
        pass


class Factory1990(AbsFactory):

    def create_auto(self):
        return Auto1990()

    def create_plan(self):
        return Plane1990()


class Factory2000(AbsFactory):

    def create_auto(self):
        return Auto2000()

    def create_plan(self):
        return Plane2000()


if __name__ == '__main__':

    # Создадим с помощь абстрактной фабрики фабрику 2000 года и выпустим на ней технику
    factory1 = AbsFactory.create_factory(2000)
    my_auto1 = factory1.create_auto()
    my_plan1 = factory1.create_plan()
    print(my_auto1.run())
    print(my_plan1.run())

    # Создадим с помощь абстрактной фабрики фабрику 1990 года и выпустим на ней технику
    factory2 = AbsFactory.create_factory(1990)
    my_auto2 = factory2.create_auto()
    my_plan2 = factory2.create_plan()
    print(my_auto2.run())
    print(my_plan2.run())
