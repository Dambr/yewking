# Генерация матрицы трассируемости требований на файлы исходного кода 

from random import randint, shuffle
import numpy as np


class GeneratorT():
    # min_value - минимальное число файлов, которые реализуют одно требование
    # max_value - максимальное число файлов, которые реализуют одно требование
    def __init__(self, n, m, min_value, max_value):
        self.n = n
        self.m = m
        self.min_value = min_value
        self.max_value = max_value

    def generate(self):
        n = self.n
        m = self.m
        get_traced_data = self.__get_traced_data

        result = []
        for _ in range(n):
            data = get_traced_data()
            count = data[0]
            value = data[1]

            traced_list = np.zeros(m)
            for i in range(m):
                if i < count:
                    traced_list[i] = value
            shuffle(traced_list)
            result.append(traced_list)
        return np.array(result)

    def __get_traced_data(self):
        min_value = self.min_value
        max_value = self.max_value

        count = 0
        value = 0
        while True:
          count = randint(min_value, max_value)
          value = 1 / count
          if count * value == 1:
            break
        return (count, value)