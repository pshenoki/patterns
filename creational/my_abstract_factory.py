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


class Plane1999(Transport):

    def run(self):
        return 'plane 1999 run'


class Auto1999(Transport):

    def run(self):
        return 'auto 1999 run'


class AbsFactory(ABC):

    @staticmethod
    def create_factory(model):

        MODELS = {
            1990: Factory1990(),
            1999: Factory1999()

        }
        return MODELS[model]

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


class Factory1999(AbsFactory):

    def create_auto(self):
        return Auto1999()

    def create_plan(self):
        return Plane1999()


if __name__ == '__main__':
    factory = AbsFactory.create_factory(1999)
    my_auto = factory.create_auto()
    my_plan = factory.create_plan()

    print(my_auto.run())
    print(my_plan.run())

    factory = AbsFactory.create_factory(1990)
    my_auto = factory.create_auto()
    my_plan = factory.create_plan()

    print(my_auto.run())
    print(my_plan.run())
