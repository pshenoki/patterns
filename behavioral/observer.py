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
    def call(self, shop):
        pass

    def subscription(self, shop):
        shop.attach(self)


class MtsShop(Shop):
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
            observer.call(self)

    def update_menu(self, new_position):
        self.menu.append(new_position)
        print(f"добавлена новая позиция: {new_position}")


class IPhoneChecker(Client):

    def call(self, shop):
        if 'iphone' in shop.menu:
            print(f'{self.name} оповещен о наличии IPhone в магазине {shop.name}')


class IPadChecker(Client):

    def call(self, shop):
        if 'ipad' in shop.menu:
            print(f'{self.name} оповещен о наличии IPad в магазине {shop.name}')


if __name__ == '__main__':
    # Создаем обьекты магазина и клиентов
    mts_shop = MtsShop('МТС')
    iphone_client = IPhoneChecker("Вася")
    ipad_client = IPadChecker("Петя")

    # Подключаемся на подписку к магазину
    iphone_client.subscription(mts_shop)
    ipad_client.subscription(mts_shop)
    print('-' * 20)

    # Добавляем товар, на который никто не подписан, включаем оповещение
    mts_shop.update_menu('macbook')
    mts_shop.notify()
    print('-' * 20)

    # Добавляем товар iphone, включаем оповещение
    mts_shop.update_menu('iphone')
    mts_shop.notify()
    print('-' * 20)

    # Добавляем товар ipad, включаем оповещение
    mts_shop.update_menu('ipad')
    mts_shop.notify()
