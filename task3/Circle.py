import math


class Circle:
    """Класс для представления круга с координатами центра и радиусом."""

    def __init__(self, x, y, radius):
        self.center = (x, y)
        self.radius = radius
