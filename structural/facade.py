from abc import ABC, abstractmethod


class Checker(ABC):

    @staticmethod
    @abstractmethod
    def milk_price_check():
        pass

    @staticmethod
    @abstractmethod
    def bread_price_check():
        pass


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


class ShopFacade:
    def __init__(self, *args):
        self.check_list = [checker for checker in args if isinstance(checker, Checker)]

    def check_milk_min(self):
        min_price = min([checker.milk_price_check() for checker in self.check_list])
        return min_price

    def check_bread_min(self):
        min_price = min([checker.bread_price_check() for checker in self.check_list])
        return min_price


if __name__ == '__main__':
    p = PerekrestokChecker()
    v = VkusvillChecker()
    m = MarketChecker()

    grandma = ShopFacade(p, v, m, 23)
    print(grandma.check_milk_min())
    print(grandma.check_bread_min())
