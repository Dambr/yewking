# Генерация матрицы зависимостей между файлами исходного кода

from random import randint, shuffle
import numpy as np


class GeneratorD():
    # min_value - минимальное число файлов зависимостей
    # max_value - максимальное число файлов зависимостей
    def __init__(self, m, min_value, max_value):
        self.m = m
        self.min_value = min_value
        self.max_value = max_value

    def generate(self):
        m = self.m
        min_value = self.min_value
        max_value = self.max_value

        result = []
        for _ in range(m):
          count = randint(min_value, max_value)
          dependencies = np.zeros(m)
          for i in range(m):
            if i < count:
              dependencies[i] = 1
          shuffle(dependencies)
          result.append(dependencies)
        return np.array(result)