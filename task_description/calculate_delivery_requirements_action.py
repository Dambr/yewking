# Рассчет реализованных в поставке требований

import numpy as np


class CalculateDeliveryRequirementsAction():
    def __init__(self, calculate_delivery_files_action, implement_checker, T):
        self.calculate_delivery_files_action = calculate_delivery_files_action
        self.implement_checker = implement_checker
        self.T = T

    def calculate(self):
        calculate_delivery_files_action = self.calculate_delivery_files_action
        implement_checker = self.implement_checker
        T = self.T

        delivery_files = calculate_delivery_files_action.calculate()
        delivery_requirements = np.dot(T, delivery_files)
        result = implement_checker.check(delivery_requirements)
        return result