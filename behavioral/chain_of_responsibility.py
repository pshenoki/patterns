""" Задача:
        1. Создать класс Сообщение.
        2. Создать классы Оператор, который бы проверял наличие в сообщении определеных букв.
        3. Организовать возможность подключения операторов.
    Паттерн:
        Цепочка обязанностей (Chain of responsibility) """

from abc import ABC, abstractmethod


class Handler(ABC):
    """ абстрактный класс для всех операторов """
    def __init__(self):
        self.next_handler = None

    @abstractmethod
    def handle(self, message):
        if self.next_handler:
            self.next_handler.handle(message)

    def link(self, handler):
        self.next_handler = handler
        return handler


class Message:
    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message


class Operator(Handler):

    def __init__(self, letter):
        super().__init__()
        self.letter = letter

    def handle(self, message):
        if self.letter in message:
            print(f'Буква "{self.letter}" есть в слове {message}')
        else:
            print(f'Буква "{self.letter}" отсутствует в слове {message}')
        super().handle(message)


if __name__ == '__main__':
    # Создаем сообщение
    my_message = Message('hello world')

    # Создаем оператора (проверяющего букву "a") и подключаем к нему других операторов
    my_handler = Operator('a')
    my_handler.link(Operator("b")). \
        link(Operator("c")). \
        link(Operator("d")). \
        link(Operator("e")). \
        link(Operator("f")). \
        link(Operator("g")). \
        link(Operator("h"))

    # Вызываем метод проверки
    my_handler.handle(my_message.get_message())

    """ Что получается:
            1. Во время установки ссылок (.link) мы каждому оператору (кроме последнего) передали следующего оператора
            2. То есть у Operator('a') стоит next_handler Operator('b') и т.д. У Operator('h') так и осталось None
            3. Мы по очереди вызываем метод handle у операторов. Сначала выполняется метод обьекта, после чего метод 
            родителя, а именно метод handle класса Handler(ABC)
            4 Он смотрит, есть ли у нас следующий operator, и если есть, вызывает у него метод handle и так далее
             пока не дойдем до последнего, после чего программа завершается."""

