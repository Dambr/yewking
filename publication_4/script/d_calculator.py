import numpy as np

class DCalculator():

    def __init__(self, dependencies, files_tokenizer, m_calculator):
        self.dependencies_data = dependencies
        self.files_tokenizer = files_tokenizer
        self.m_calculator = m_calculator

    def calculate(self):
        dependencies_data = self.dependencies_data
        files_tokenizer = self.files_tokenizer
        m_calculator = self.m_calculator

        m = m_calculator.calculate()

        result = np.zeros((m, m))

        for data in dependencies_data:
            file = data['file']
            dependencies = data['dependencies']

            file_token = files_tokenizer.get_token(file)
            for dependency in dependencies:
                dependency_token = files_tokenizer.get_token(dependency)
                result[file_token][dependency_token] = 1

        return result
