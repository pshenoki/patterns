""" Задача:
        1. Создать магазин с возможным добавление в него товаров.
        2. Создать покупателей с оформлением и отменой подписки на магазин.
        3. Покупатель должен отслеживать конкретный товар.
        4. При наличие товара информировать соответствующих покупателей.
    Паттерн:
        Наблюдатель (Observer) """

from abc import ABC, abstractmethod


class Shop(ABC):
    """ абстрактный класс для всех магазинов """

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Client(ABC):
    """ абстрактный класс для всех покупателей """
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def check(self, shop):
        pass

    def subscribe(self, shop):
        shop.attach(self)

    def unsubscribe(self, shop):
        shop.detach(self)


class MtsShop(Shop):
    """ Конкретный магазин """
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.observers = set()

    def attach(self, observer):
        self.observers.add(observer)
        print(f'{observer.name} подписался на обновления магазина {self.name}')

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.check(self)

    def update_menu(self, new_position):
        self.menu.append(new_position)
        print(f"В магазин {self.name} добавлена новая позиция: {new_position}")


class BeelineShop(MtsShop):
    """ создадим еще один магазин """
    pass


class IPhoneChecker(Client):
    """ клиента, который подписан на обновления IPhone"""
    def check(self, shop):
        if 'iphone' in shop.menu:
            print(f'{self.name} оповещен о наличии IPhone в магазине {shop.name}')


class IPadChecker(Client):
    """ клиента, который подписан на обновления IPad"""
    def check(self, shop):
        if 'ipad' in shop.menu:
            print(f'{self.name} оповещен о наличии IPad в магазине {shop.name}')


if __name__ == '__main__':
    # Создаем обьекты магазина и клиентов
    mts_shop = MtsShop('МТС')
    beeline_shop = BeelineShop('Билайн')
    iphone_client = IPhoneChecker("Вася")
    ipad_client = IPadChecker("Петя")

    # Подключаемся на подписку к магазину
    iphone_client.subscribe(mts_shop)
    ipad_client.subscribe(mts_shop)
    iphone_client.subscribe(beeline_shop)
    ipad_client.subscribe(beeline_shop)
    print('-' * 20)

    # Добавляем товар, на который никто не подписан, включаем оповещение
    mts_shop.update_menu('macbook')
    mts_shop.notify()
    beeline_shop.update_menu('macbook')
    beeline_shop.notify()
    print('-' * 20)

    # Добавляем товар iphone, включаем оповещение
    mts_shop.update_menu('iphone')
    mts_shop.notify()
    beeline_shop.update_menu('iphone')
    beeline_shop.notify()
    print('-' * 20)

    # Добавляем товар ipad, включаем оповещение
    mts_shop.update_menu('ipad')
    mts_shop.notify()
    beeline_shop.update_menu('ipad')
    beeline_shop.notify()
    print('-' * 20)

    # Отменяем подписку Васи на магазины, включаем оповещение
    iphone_client.unsubscribe(mts_shop)
    iphone_client.unsubscribe(beeline_shop)
    mts_shop.notify()
    beeline_shop.notify()
