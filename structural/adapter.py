from abc import ABC


class Translator(ABC):
    @staticmethod
    def tell_something(name):
        return f"My name is {name}"


class Russian:
    def __init__(self, name):
        self.name = name

    def tell_the_name(self):
        return f'Меня зовут {self.name}'


class RussianLearningEng(Russian, Translator):
    def tell_the_name(self):
        return self.tell_something(self.name)


if __name__ == '__main__':
    russian = Russian('Иван')
    russian_a1 = RussianLearningEng('Артем')
    print(russian.tell_the_name())
    print(russian_a1.tell_the_name())

