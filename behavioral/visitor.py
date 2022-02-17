""" Задача:
        1. Создать класс машин (Ауди и Лексус) c возможностью принимать инженера.
        2. Создать инженера, который в машины устанавливает детали согдасно их маркам.
    Паттерн:
        Посетитель (visitor) """

from abc import ABC, abstractmethod


class Car(ABC):
    """ абстрактный класс для всех машин """
    def __init__(self):
        self.car_body = []

    def add_component(self, component):
        self.car_body.append(component)

    @abstractmethod
    def accept(self, visitor):
        pass


class Lexus(Car):

    def show_car(self):
        print(f'Lexus: {self.car_body}')

    def accept(self, visitor):
        visitor.visit_lexus_car(self)


class Audi(Car):

    def show_car(self):
        print(f'Audi: {self.car_body}')

    def accept(self, visitor):
        visitor.visit_audi_car(self)


class Engineer(ABC):
    """ абстрактный класс для всех инженеров """
    @abstractmethod
    def visit_audi_car(self, audi_car):
        pass

    @abstractmethod
    def visit_lexus_car(self, lexus_element):
        pass


class WheelEngineer(Engineer):
    """ Инженер, который устанавливает колеса """
    def visit_audi_car(self, audi_car):
        audi_car.add_component('audi_wheels')

    def visit_lexus_car(self, lexus_car):
        lexus_car.add_component('lexus_wheels')


class EngineEngineer(Engineer):
    """ Инженер, который устанавливает двигатель """
    def visit_audi_car(self, audi_car):
        audi_car.add_component('audi_engine')

    def visit_lexus_car(self, lexus_car):
        lexus_car.add_component('lexus_engine')


class UniversalEngineer(Engineer):
    """ Универсальный инженер, который устанавливает, что попросят """
    def __init__(self, component):
        self.component = component

    def visit_audi_car(self, audi_car):
        audi_car.add_component(f'audi_{self.component}')

    def visit_lexus_car(self, lexus_car):
        lexus_car.add_component(f'lexus_{self.component}')


if __name__ == '__main__':

    # Создаем инженеров (универсальный инженер будет устанавливать колеса)
    wheel_engineer = WheelEngineer()
    engine_engineer = EngineEngineer()
    universal_engineer = UniversalEngineer('doors')

    # Создаем машины и смотрим внутренности
    car_audi = Audi()
    car_lexus = Lexus()
    car_audi.show_car()
    car_lexus.show_car()
    print('-' * 20)

    # Приглашаем инженера по колесам
    car_audi.accept(wheel_engineer)
    car_lexus.accept(wheel_engineer)
    car_audi.show_car()
    car_lexus.show_car()
    print('-' * 20)

    # Приглашаем инженера по двигателям
    car_audi.accept(engine_engineer)
    car_lexus.accept(engine_engineer)
    car_audi.show_car()
    car_lexus.show_car()
    print('-' * 20)

    # Приглашаем универсального инженера для установки дверей
    car_audi.accept(universal_engineer)
    car_lexus.accept(universal_engineer)
    car_audi.show_car()
    car_lexus.show_car()
