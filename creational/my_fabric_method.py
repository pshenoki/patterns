""" Паттерн:
        Фабричный метод (Fabric method)
    Суть паттерна:
        Паттерн "Фабричный метод" определяет общий интерфейс для создания объектов в суперклассе,
        позволяя подклассам изменять тип создаваемых объектов.
    Задача:
        1. Создать класс Фабрика, который бы управлял созданием нужного вида транспорта. """

from abc import abstractmethod, ABC


class Transport(ABC):
    """ абстрактный класс для всех видов транспорта """
    @abstractmethod
    def run(self):
        pass


class Auto(Transport):

    def run(self):
        return 'run on road'


class Plan(Transport):

    def run(self):
        return 'run on air'


class Ship(Transport):

    def run(self):
        return 'run on sea'


class TransportFactory:
    transport_dict = {
                    'auto': Auto(),
                    'airplane': Plan(),
                    'ship': Ship()
                     }

    def create_transport(self, transport):
        return self.transport_dict[transport]


if __name__ == '__main__':
    # Создаем класс фабрика
    factory = TransportFactory()

    # Создаем обьекты транспорта
    car = factory.create_transport('auto')
    plane = factory.create_transport('airplane')
    boat = factory.create_transport('ship')

    # Запускаем транспорт
    print(car.run())
    print(plane.run())
    print(boat.run())
