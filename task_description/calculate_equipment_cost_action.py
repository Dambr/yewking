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

        R = calculate_delivery_requirements_action.calculate()
        # costs = np.dot(C, delivery_requirements)
        result = bin_multiply(C, R)
        return result
    
    def __bin_multiply(self, C, R):
        add_multiply_constraints_action = self.add_multiply_constraints_action

        result = []
        cashed = {}
        n = len(R)

        # сначала перемножаем переменные попарно
        for i in range(n):
            for j in range(n):
                record = (i, j)
                contains = record in cashed
                if not contains:
                    r_i = R[i]
                    r_j = R[j]
                    f = add_multiply_constraints_action.add_multiply_constraints(r_i, r_j)
                    reverse_record = (j, i)
                    cashed[record] = f
                    cashed[reverse_record] = f

        # теперь умножаем элементы матрицы на переменные
        for i in range(n):
            for j in range(n):
                record = (i, j)
                f = cashed[record]
                element = C[i][j] * f
                result.append(element)

        return sum(result)
        
        # result = []
        # length = len(vector1)
        # for i in range(length):
        #     p1 = vector1[i]
        #     p2 = vector2[i]
        #     f = add_multiply_constraints_action.add_multiply_constraints(p1, p2)
        #     result.append(f)
        # return sum(result)