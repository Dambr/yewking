import numpy as np

class FitnessCalculator:
    def __init__(self, M, cost_calculator_factory, converter):
        self.M = M
        self.cost_calculator_factory = cost_calculator_factory
        self.converter = converter

    def calculate(self, solution):
        A = self.converter.convert(solution)
        valid = self.__validate(A)
        fitness = -self.M
        if (valid):
            cost_calculator = self.cost_calculator_factory.get_cost_calculator(A)
            cost = cost_calculator.calculate()
            fitness = -cost
        return fitness

    def __validate(self, A):
        result = True
        for row in A:
            if np.sum(row) != 1:
                result = False
        return result
        