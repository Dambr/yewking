# Рассчет полезных файлов исходного кода и их зависимостей

import numpy as np


class CalculateUsefulFilesAction():
    def __init__(self, useful_requirements, T, sum_D):
        self.useful_requirements = useful_requirements
        self.T = T
        self.sum_D = sum_D

    def calculate(self):
        useful_requirements = self.useful_requirements
        T = self.T
        sum_D = self.sum_D
        
        normalize = lambda x: 0 if x == 0 else 1
        useful_files = np.dot(useful_requirements, T)
        useful_files = np.dot(useful_files, sum_D)
        
        result = np.array([normalize(x) for x in useful_files])
        
        return result