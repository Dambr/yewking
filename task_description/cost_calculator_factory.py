from cost_calculator import CostCalculator

class CostCalculatorFactory:
    def __init__(self, T, deps, C, E):
        self.T = T
        self.deps = deps
        self.C = C
        self.E = E

    def get_cost_calculator(self, A):
        cost_calculator = CostCalculator(self.T, self.deps, self.C, self.E, A)
        return cost_calculator