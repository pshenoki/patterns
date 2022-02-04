from abc import ABC, abstractmethod


class Machine(ABC):
    @abstractmethod
    def make_word(self):
        pass


class PrintMachine(Machine):
    def __init__(self, word):
        self.word = word

    def make_word(self):
        return self.word


class AbsDecor(Machine, ABC):
    def __init__(self, machine):
        self.machine = machine

    @abstractmethod
    def make_word(self):
        pass


class StarDecor(AbsDecor):

    def __call__(self, *args, **kwargs):
        return self.make_word()

    def make_word(self):
        return '* ' + self.machine.make_word() + ' *'


class SlashDecor(AbsDecor):

    def make_word(self):
        return '/ ' + self.machine.make_word() + ' /'


@StarDecor
class PrintMachine2(PrintMachine):
    pass


if __name__ == '__main__':
    printer_hello = PrintMachine('hello')
    print(printer_hello.make_word())

    dec_printer = StarDecor(printer_hello)
    print(dec_printer.make_word())

    dec_slash_printer = SlashDecor(dec_printer)
    print(dec_slash_printer.make_word())

    printer_2 = PrintMachine2('aaa')
    print(printer_2.make_word())
