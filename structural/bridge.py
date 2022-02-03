from abc import ABC, abstractmethod


class DrawingColor(ABC):
    @abstractmethod
    def draw_color(self, x, y, name):
        pass


class DrawingRed(DrawingColor):
    def draw_color(self, x, y, name):
        print(f'Red color figure {name} with center {x}:{y}')


class DrawingGreen(DrawingColor):
    def draw_color(self, x, y, name):
        print(f'Green color figure {name} with center {x}:{y}')


class Figure(ABC):

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def draw_inversion(self):
        pass


class Circle(Figure):
    def __init__(self, x, y, color_draw):
        self.name = 'Circle'
        self._x = x
        self._y = y
        self.color_draw = color_draw

    def draw(self):
        self.color_draw.draw_color(name=self.name, x=self._x, y=self._y)

    def draw_inversion(self):
        self.color_draw.draw_color(name=self.name, x=self._x * -1, y=self._y * -1)


class Square(Figure):
    def __init__(self, x, y, color_draw):
        self.name = 'Square'
        self._x = x
        self._y = y
        self.color_draw = color_draw

    def draw(self):
        self.color_draw.draw_color(name=self.name, x=self._x, y=self._y)

    def draw_inversion(self):
        self.color_draw.draw_color(name=self.name, x=self._x * -1, y=self._y * -1)


if __name__ == '__main__':
    shapes = [Circle(1, 1, DrawingRed()),
              Circle(2, 2, DrawingGreen()),
              Square(3, 3, DrawingRed()),
              Square(4, 4, DrawingGreen())
              ]

    for shape in shapes:
        shape.draw()
        shape.draw_inversion()
        print("*" * 15)
