# Рассчет стоимости сопровождения и поддержки поставки

import numpy as np


class CalculateEquipmentCostAction():
    def __init__(self, calculate_delivery_requirements_action, add_multiply_constraints_action, P):
        self.calculate_delivery_requirements_action = calculate_delivery_requirements_action
        self.add_multiply_constraints_action = add_multiply_constraints_action
        self.P = P

    def calculate(self):
        calculate_delivery_requirements_action = self.calculate_delivery_requirements_action
        bin_multiply = self.__bin_multiply
        P = self.P

        delivery_requirements = calculate_delivery_requirements_action.calculate()
        costs = np.dot(P, delivery_requirements)
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
        # result = []
        # for row_number in range(rows_count):
        #     matrix_row = matrix[row_number]
        #     terms = []
        #     for col_number in range(cols_count):
        #         vector_element = vector[col_number]
        #         matrix_element = matrix_row[col_number]
        #         term = add_multiply_constraints_action.add_multiply_constraints(vector_element, matrix_element)
        #         terms.append(term)
        #     sum_terms = sum(terms)
        #     result.append(sum_terms)
        # return np.array(result)