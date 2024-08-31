# Рассчет включаемых в поставку плагинов

import numpy as np


class CalculatePluginsAction():
    def __init__(self, calculate_useful_files_action, include_checker, A):
        self.calculate_useful_files_action = calculate_useful_files_action
        self.include_checker = include_checker
        self.A = A

    def calculate(self):
        calculate_useful_files_action = self.calculate_useful_files_action
        include_checker = self.include_checker
        A = self.A

        useful_files = calculate_useful_files_action.calculate()
        plugins = np.dot(useful_files, A)
        result = include_checker.check(plugins)
        return result