from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Lexus(Car):
    def __init__(self):
        self.car_body = []

    def show_car(self):
        print(f'Lexus: {self.car_body}')

    def accept(self, visitor):
        visitor.visit_lexus_car(self)


class Audi(Car):
    def __init__(self):
        self.car_body = []

    def show_car(self):
        print(f'Audi: {self.car_body}')

    def accept(self, visitor):
        visitor.visit_audi_car(self)


class Engineer(ABC):
    @abstractmethod
    def visit_audi_car(self, audi_car):
        pass

    @abstractmethod
    def visit_lexus_car(self, lexus_element):
        pass


class WheelEngineer(Engineer):
    def visit_audi_car(self, audi_car):
        audi_car.car_body.append('audi_wheels')

    def visit_lexus_car(self, lexus_car):
        lexus_car.car_body.append('lexus_wheels')


class EngineEngineer(Engineer):
    def visit_audi_car(self, audi_car):
        audi_car.car_body.append('audi_engine')

    def visit_lexus_car(self, lexus_car):
        lexus_car.car_body.append('lexus_engine')


class UniversalEngineer(Engineer):
    def __init__(self, component):
        self.component = component

    def visit_audi_car(self, audi_car):
        audi_car.car_body.append(f'audi_{self.component}')

    def visit_lexus_car(self, lexus_car):
        lexus_car.car_body.append(f'lexus_{self.component}')


if __name__ == '__main__':
    """ создаем инженеров"""
    wheel_engineer = WheelEngineer()
    engine_engineer = EngineEngineer()
    universal_engineer = UniversalEngineer('doors')

    """ создаем машины и смотрим внутренности"""
    car_audi = Audi()
    car_lexus = Lexus()
    car_audi.show_car()
    car_lexus.show_car()
    print('-----------------------------')
    """ приглашаем инженера по колесам"""
    car_audi.accept(wheel_engineer)
    car_lexus.accept(wheel_engineer)
    car_audi.show_car()
    car_lexus.show_car()
    print('-----------------------------')
    """ приглашаем инженера по двигателям"""
    car_audi.accept(engine_engineer)
    car_lexus.accept(engine_engineer)
    car_audi.show_car()
    car_lexus.show_car()
    print('-----------------------------')
    """ приглашаем инженера универсального"""
    car_audi.accept(universal_engineer)
    car_lexus.accept(universal_engineer)
    car_audi.show_car()
    car_lexus.show_car()
