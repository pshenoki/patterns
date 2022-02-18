""" Задача:
        1. Создать класс Заказ, с возможность добавления в него продукта.
        2. Организовать стратегию оплаты разными способами.
    Паттерн:
        Стратегия (Strategy) """

from abc import ABC, abstractmethod


class Order:
    """ Класс заказ"""
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    """ Стратегия оплаты """
    def pay(self, strategy):
        total = self.get_total()
        strategy.pay(total)
        print('Покупка завершена успешно')


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class PaymentStrategy(ABC):
    """ абстрактный класс для всех стратегий оплаты """
    @abstractmethod
    def pay(self, amount):
        pass


class PayPalPaymentStrategy(PaymentStrategy):
    """ Оплата с учетной записи """
    def __init__(self, email, token):
        self.email = email
        self.token = token

    def pay(self, amount):
        print(f'проводим оплату суммы {amount} р. c аккаунта: {self.email}')


class CreditCardPaymentStrategy(PaymentStrategy):
    """ Оплата картой """
    def __init__(self, card):
        self.card = card

    def pay(self, amount):
        print(f'проводим оплату суммы {amount} р. c карты: {self.card}')


if __name__ == '__main__':

    # Создаем заказ и добавляем в него продукты
    order = Order()
    item1 = Item("Book", 200)
    item2 = Item("Magazine", 300)
    order.add_item(item1)
    order.add_item(item2)

    # Выбор стратегии Paypal и оплата заказа
    paypal_payment_strategy = PayPalPaymentStrategy("strategy@patterns.com", "token")
    order.pay(paypal_payment_strategy)
    print('-' * 20)

    # выбор стратегии CreditCard и оплата заказа
    credit_card_payment_strategy = CreditCardPaymentStrategy('1234 5678 9101 2131 4156')
    order.pay(credit_card_payment_strategy)
