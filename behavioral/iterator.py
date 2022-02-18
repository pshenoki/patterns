""" Задача:
        1. Создать класс со сложной структурой.
        2. Реализовать возможность пройти в цикле по ней, создав класс Итератор.
    Паттерн:
        Итератор (Iterator) """

from collections.abc import Iterable, Iterator


class StrongCollection(Iterable):
    """ Итерируемый класс"""

    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        return StrongIterator(self.collection)


class StrongIterator(Iterator):
    """ Итератор """

    def __init__(self, container):
        self.result = []
        self.recursive_unpack(container)
        self.n = -1

    def recursive_unpack(self, container):
        for el in container:
            if isinstance(el, Iterable) and not isinstance(el, str):
                self.recursive_unpack(el)
            else:
                self.result.append(el)

    def __next__(self):
        self.n += 1
        if self.n < len(self.result):
            return self.result[self.n]
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':

    # Создаем структуру данных и проходимся в цикле
    structure = StrongIterator([1, '1,5', 2, [[3, '4,25'], 5, [6.8, 7]], [[[8]]], 9])
    for i in structure:
        print(i)
