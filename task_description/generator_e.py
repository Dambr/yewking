# Генерация матрицы комплектаций

from random import randint, shuffle
import numpy as np


class GeneratorE():
    # min_value - минимальное число полезных требований в комплектации
    # max_value - максимальное число полезных требований в комплектации
    def __init__(self, l, n, min_value, max_value):
        self.l = l
        self.n = n
        self.min_value = min_value
        self.max_value = max_value

    def generate(self):
        l = self.l
        n = self.n
        min_value = self.min_value
        max_value = self.max_value

        equipments = []
        for equipment_number in range(l):
          total_count = randint(min_value, max_value)
          requirements = np.zeros(n)
          for i in range(n):
            if i < total_count:
              requirements[i] = 1
          shuffle(requirements)
          equipments.append(requirements)
        return np.array(equipments)