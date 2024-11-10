# Рассчет полезных файлов исходного кода и их зависимостей

import numpy as np


class CalculateUsefulFilesAction():
    def __init__(self, useful_requirements, T, D):
        self.useful_requirements = useful_requirements
        self.T = T
        self.D = D

    def calculate(self):
        useful_requirements = self.useful_requirements
        T = self.T
        calculate_dependencies = self.__calculate_dependencies

        useful_files = np.dot(useful_requirements, T)
        m = len(useful_files)
        for i in range(m):
            dependencies = calculate_dependencies(i)
            useful_files += dependencies

        normalize = lambda x: 0 if x == 0 else 1
        result = np.array([normalize(x) for x in useful_files])
        
        return result

    def __calculate_dependencies(self, i):
        useful_requirements = self.useful_requirements
        T = self.T
        D = self.D
        calculate_dependencies = self.__calculate_dependencies
        
        if i == 0:
            useful_files = np.dot(useful_requirements, T)
            return np.dot(useful_files, D)
        else:
            dependencies = calculate_dependencies(i - 1)
            return np.dot(dependencies, D)