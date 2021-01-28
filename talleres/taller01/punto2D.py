#!/usr/bin/python
import math

class Punto2D():
    """Representacion de punto en 2 dimensiones"""

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
       return __x

    def get_y(self):
       return __y

    def radio_polar(self):
       return math.sqrt(x**2 + y**2) 

    def angulo_polar(self):
       return math.atan(x/y)

    def dist_euclidiana(self, other):
        dx = self.__x - other.get_x()
        dy = self.__y - other.get_y()
        return math.sqrt((dx**2) + (dy**2))