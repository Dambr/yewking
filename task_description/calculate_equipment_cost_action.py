# Рассчет стоимости сопровождения и поддержки поставки

import numpy as np


class CalculateEquipmentCostAction():
    def __init__(self, calculate_delivery_requirements_action, P):
        self.calculate_delivery_requirements_action = calculate_delivery_requirements_action
        self.P = P

    def calculate(self):
        calculate_delivery_requirements_action = self.calculate_delivery_requirements_action
        P = self.P

        delivery_requirements = calculate_delivery_requirements_action.calculate()
        costs = np.dot(P, delivery_requirements)
        result = sum(costs)
        return result