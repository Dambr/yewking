# Рассчет включаемых в поставку файлов исходного кода

import numpy as np


class CalculateDeliveryFilesAction():
    def __init__(self, calculate_plugins_action, add_multiply_constraints_action, A):
        self.calculate_plugins_action = calculate_plugins_action
        self.add_multiply_constraints_action = add_multiply_constraints_action
        self.A = A

    def calculate(self):
        calculate_plugins_action = self.calculate_plugins_action
        A = self.A
        bin_multiply = self.__bin_multiply
        
        plugins = calculate_plugins_action.calculate()
        result = bin_multiply(A, plugins)
        return result

    def __bin_multiply(self, matrix, vector):
        add_multiply_constraints_action = self.add_multiply_constraints_action
        
        (rows_count, cols_count) = np.shape(matrix)
        result = []
        for row_number in range(rows_count):
            matrix_row = matrix[row_number]
            terms = []
            for col_number in range(cols_count):
                vector_element = vector[col_number]
                matrix_element = matrix_row[col_number]
                term = add_multiply_constraints_action.add_multiply_constraints(vector_element, matrix_element)
                terms.append(term)
            sum_terms = sum(terms)
            result.append(sum_terms)
        return np.array(result)