# Генерация матрицы комплектаций

from random import randint, shuffle
import numpy as np


class GeneratorE():
    # min_value - минимальное число полезных требований в комплектации
    # max_value - максимальное число полезных требований в комплектации
    def __init__(self, e, n, min_value, max_value):
        self.e = e
        self.n = n
        self.min_value = min_value
        self.max_value = max_value

    def generate(self):
        e = self.e
        n = self.n
        min_value = self.min_value
        max_value = self.max_value

        equipments = []
        for equipment_number in range(e):
          total_count = randint(min_value, max_value)
          requirements = np.zeros(n)
          for i in range(n):
            if i < total_count:
              requirements[i] = 1
          shuffle(requirements)
          equipments.append(requirements)
        return np.array(equipments)