import numpy as np

class CCalculator():

    def __init__(self, n_calculator):
        self.n_calculator = n_calculator

    def calculate(self):
        n_calculator = self.n_calculator

        n = n_calculator.calculate()

        return np.eye(n)
