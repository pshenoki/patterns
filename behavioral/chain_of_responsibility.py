from abc import ABC, abstractmethod


class Handler(ABC):
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
    my_message = Message('hello world')

    my_handler = Operator('a')
    my_handler.link(Operator("b")). \
        link(Operator("c")). \
        link(Operator("d")). \
        link(Operator("e")). \
        link(Operator("f")). \
        link(Operator("g")). \
        link(Operator("h"))

    my_handler.handle(my_message.get_message())
