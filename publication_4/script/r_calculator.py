import numpy as np

class RCalculator():

    def __init__(self, complectations, requirements_tokenizer, n_calculator):
        self.complectations = complectations
        self.requirements_tokenizer = requirements_tokenizer
        self.n_calculator = n_calculator

    def calculate(self):
        complectations = self.complectations['complectations']
        requirements_tokenizer = self.requirements_tokenizer
        n_calculator = self.n_calculator

        n = n_calculator.calculate()

        result = []

        for complectation in complectations:
            row = np.zeros(n)

            requirements = complectation['requirements']
            for requirement in requirements:
                token = requirements_tokenizer.get_token(requirement)
                row[token] = 1

            result.append(row)

        return np.array(result)
