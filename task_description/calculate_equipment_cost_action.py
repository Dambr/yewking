# Рассчет стоимости сопровождения и поддержки поставки

import numpy as np


class CalculateEquipmentCostAction():
    def __init__(self, calculate_delivery_requirements_action, add_multiply_constraints_action, C):
        self.calculate_delivery_requirements_action = calculate_delivery_requirements_action
        self.add_multiply_constraints_action = add_multiply_constraints_action
        self.C = C

    def calculate(self):
        calculate_delivery_requirements_action = self.calculate_delivery_requirements_action
        bin_multiply = self.__bin_multiply
        C = self.C

        delivery_requirements = calculate_delivery_requirements_action.calculate()
        costs = np.dot(C, delivery_requirements)
        result = bin_multiply(delivery_requirements, costs)
        return result
    
    def __bin_multiply(self, vector1, vector2):
        add_multiply_constraints_action = self.add_multiply_constraints_action
        
        result = []
        length = len(vector1)
        for i in range(length):
            p1 = vector1[i]
            p2 = vector2[i]
            f = add_multiply_constraints_action.add_multiply_constraints(p1, p2)
            result.append(f)
        return sum(result)