# Генерация матрицы изменения стоимостей сопровождения и поддержки требований в поставке

from random import randint
import numpy as np


class GeneratorC():
    # min_value - минимальное значение стоимости сопровождения единицы функционала
    # max_value - максимальное значение стоимости сопровождения единицы функционала
    def __init__(self, n, min_value, max_value):
        self.n = n
        self.min_value = min_value
        self.max_value = max_value

    def generate(self):
        n = self.n
        min_value = self.min_value
        max_value = self.max_value

        result = np.identity(n, dtype=float)
        for i in range(n):
            for j in range(n):
                if i != j:
                    value = randint(min_value, max_value)
                    result[i][j] = value
        
        return result