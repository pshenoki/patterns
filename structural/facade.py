""" Паттерн:
        Фасад (Facade)
    Суть паттерна:
        Паттерн "Фасад" предоставляет простой интерфейс к сложной системе классов, библиотеке или фреймворку.
    Задача:
        1. Создать класс Проверяющий, который бы из магазина узнавал цену конкретного товара.
        2. Создать класс Фасад, который бы выбирал минимальную цену среди всех магазинов. """

from abc import ABC, abstractmethod


class Checker(ABC):
    """ Абстрактный класс для всех проверяющих """
    @staticmethod
    @abstractmethod
    def milk_price_check():
        pass

    @staticmethod
    @abstractmethod
    def bread_price_check():
        pass


# Опустим логику получения цены из магазина и для простоты будем просто получать цену и название магазина
class PerekrestokChecker(Checker):
    @staticmethod
    def milk_price_check():
        return 100, 'milk from perekrestok'

    @staticmethod
    def bread_price_check():
        return 25, 'bread from perekrestok'


class VkusvillChecker(Checker):
    @staticmethod
    def milk_price_check():
        return 200, 'milk from vkusvill'

    @staticmethod
    def bread_price_check():
        return 100, 'bread from vkusvill'


class MarketChecker(Checker):
    @staticmethod
    def milk_price_check():
        return 70, 'milk from market'

    @staticmethod
    def bread_price_check():
        return 30, 'bread from vkusvill'


class MinPriceFacade:
    """ Класс фасад, который принимает всех проверяющих """
    def __init__(self, *args):
        self.check_list = [checker for checker in args if isinstance(checker, Checker)]

    # Созданим методы для нахождения минимальных цен
    def check_milk_min_price(self):
        min_price = min([checker.milk_price_check() for checker in self.check_list])
        return min_price

    def check_bread_min_price(self):
        min_price = min([checker.bread_price_check() for checker in self.check_list])
        return min_price


if __name__ == '__main__':
    # Создадим проверяющих
    p = PerekrestokChecker()
    v = VkusvillChecker()
    m = MarketChecker()

    # Создадим фасад для проверки цен
    grandma = MinPriceFacade(p, v, m)
    print(grandma.check_milk_min_price())
    print(grandma.check_bread_min_price())

    """ Основной смысл фасада в том, что клиенту не хотелось бы иметь много интерфейсов для каждого магазина,
        а иметь один общий интерфейс, для выявления минимальной цены товара. """