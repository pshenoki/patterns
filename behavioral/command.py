from abc import ABC, abstractmethod
from pprint import pprint


class CommandsInvoker:
    def __init__(self):
        self._commands_list = []

    def store_command(self, command):
        self._commands_list.append(command)

    def execute_commands(self):
        for command in self._commands_list:
            command.execute()

    def undo_commands(self):
        for command in self._commands_list:
            command.undo()


class Command(ABC):
    def __init__(self, receiver):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class PutOnHat(Command):
    def execute(self):
        self._receiver.put_on_hat()

    def undo(self):
        self._receiver.put_down_hat()


class PutOnCloak(Command):
    def execute(self):
        self._receiver.put_on_cloak()

    def undo(self):
        self._receiver.put_down_cloak()


class Person:
    def __init__(self):
        self.look = {'head': 'nothing',
                     'body': 'nothing',
                     }

    def put_on_hat(self):
        self.look['head'] = 'Hat'

    def put_down_hat(self):
        self.look['head'] = 'nothing'

    def put_on_cloak(self):
        self.look['body'] = 'Cloak'

    def put_down_cloak(self):
        self.look['body'] = 'nothing'

    def show(self):
        pprint(self.look)


if __name__ == '__main__':
    commander = CommandsInvoker()
    person = Person()
    person.show()
    ''' Добавляем все команды в список команды'''
    commander.store_command(PutOnHat(person))
    commander.store_command(PutOnCloak(person))
    ''' Выполняем только execute команды'''
    commander.execute_commands()
    person.show()
    ''' Выполняем только undo команды'''
    commander.undo_commands()
    person.show()
