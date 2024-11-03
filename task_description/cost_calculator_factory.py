from cost_calculator import CostCalculator

class CostCalculatorFactory:
    def __init__(self, T, D, C, E):
        self.T = T
        self.D = D
        self.C = C
        self.E = E

    def get_cost_calculator(self, A):
        cost_calculator = CostCalculator(self.T, self.D, self.C, self.E, A)
        return cost_calculator