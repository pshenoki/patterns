""" Суть паттерна:
        Паттерн одиночка гарантирует, что у класса будет только один экземпляр,
        и предоставляет к нему глобальную точку доступа.
    Задача:
        1. Создать класс, у которого может быть только один экземпляр.
        2. Создать еще один экземпляр этого класса и проверить, что это один и тот же объект.
    Паттерн:
        Одиночка (Singleton)"""


class Singleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class RussianPresident(metaclass=Singleton):
    pass


if __name__ == '__main__':
    # Создаем президента и пытаемся создать еще одного
    putin = RussianPresident()
    medvedev = RussianPresident()
    # Проверяем...
    print(medvedev is putin)
