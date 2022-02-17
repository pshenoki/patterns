""" Задача:
        1. Создать класс командира и солдата.
        2. По команде подьем или отбой солдаты должны полность одеться или раздеться .
    Паттерн:
        Команда (Command) """

from abc import ABC, abstractmethod
from pprint import pprint


class CommandsInvoker:
    """ класс командир """
    def __init__(self):
        self._commands_list = []

    def store_command(self, command):
        self._commands_list.append(command)

    def execute_commands(self):
        print('Подъем: ')
        for command in self._commands_list:
            command.execute()

    def undo_commands(self):
        print('Отбой: ')
        for command in self._commands_list:
            command.undo()


class Command(ABC):
    """ абстрактный класс для всех команд, мы принимаем обьект над которым будет произведена команда """
    def __init__(self, receiver):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class PutOnHat(Command):
    """ Команда надеть головной убор """
    def execute(self):
        self._receiver.put_on_hat()

    def undo(self):
        self._receiver.put_down_hat()


class PutOnOverdress(Command):
    """ Команда надеть верхнюю одежду """
    def execute(self):
        self._receiver.put_on_overdress()

    def undo(self):
        self._receiver.put_down_overdress()


class Soldier(ABC):
    """ абстрактный класс для всех солдат """
    def __init__(self):
        self.look = {'head': 'nothing',
                     'body': 'nothing',
                     }

    @abstractmethod
    def put_on_hat(self):
        pass

    @abstractmethod
    def put_down_hat(self):
        pass

    @abstractmethod
    def put_on_overdress(self):
        pass

    @abstractmethod
    def put_down_overdress(self):
        pass

    def show(self):
        pprint(self.look)


class RussianSoldier(Soldier):

    def put_on_hat(self):
        self.look['head'] = 'Beret'

    def put_down_hat(self):
        self.look['head'] = 'nothing'

    def put_on_overdress(self):
        self.look['body'] = 'Сamouflage suit'

    def put_down_overdress(self):
        self.look['body'] = 'nothing'


class AmericanSoldier(Soldier):

    def put_on_hat(self):
        self.look['head'] = 'Helmet'

    def put_down_hat(self):
        self.look['head'] = 'nothing'

    def put_on_overdress(self):
        self.look['body'] = 'Military uniform'

    def put_down_overdress(self):
        self.look['body'] = 'nothing'


if __name__ == '__main__':
    # создаем командира и солдатов, смотрим в чем одеты солдаты
    commander = CommandsInvoker()
    soldier1 = RussianSoldier()
    soldier2 = AmericanSoldier()
    soldier1.show()
    soldier2.show()
    print('-' * 20)

    # Добавляем все команды в список командиру
    commander.store_command(PutOnHat(soldier1))
    commander.store_command(PutOnOverdress(soldier1))
    commander.store_command(PutOnHat(soldier2))
    commander.store_command(PutOnOverdress(soldier2))

    # Выполняем все execute команды (солдаты должны полностью одеться)
    commander.execute_commands()
    soldier1.show()
    soldier2.show()
    print('-' * 20)

    # Выполняем все undo команды (солдаты должны полностью раздеться)
    commander.undo_commands()
    soldier1.show()
    soldier2.show()
