from cost_calculator import CostCalculator

class CostCalculatorFactory:
    def __init__(self, T, sum_D, C, E):
        self.T = T
        self.sum_D = sum_D
        self.C = C
        self.E = E

    def get_cost_calculator(self, A):
        cost_calculator = CostCalculator(self.T, self.sum_D, self.C, self.E, A)
        return cost_calculator