import numpy as np
import math

class QCalculator():

    def __init__(self, tracer, files_tokenizer, requirements_tokenizer, n_calculator, m_calculator):
        self.tracer = tracer
        self.files_tokenizer = files_tokenizer
        self.requirements_tokenizer = requirements_tokenizer
        self.n_calculator = n_calculator
        self.m_calculator = m_calculator

    def calculate(self):
        tracer = self.tracer
        files_tokenizer = self.files_tokenizer
        requirements_tokenizer = self.requirements_tokenizer
        n_calculator = self.n_calculator
        m_calculator = self.m_calculator
        
        round_constant = 1000

        n = n_calculator.calculate()
        m = m_calculator.calculate()

        result = np.zeros((n, m))

        for trace in tracer:
            
            requirement = trace['requirement']
            requirement_token = requirements_tokenizer.get_token(requirement)

            files = trace['files']
            file_token_to_weight = {}
            files_count = len(files)
            max_file_index = files_count - 1
            
            file_weight = math.floor(1 / files_count * round_constant) / round_constant
            
            for file_index in range(max_file_index):
                file = files[file_index]
                file_token = files_tokenizer.get_token(file)
                file_token_to_weight[file_token] = file_weight
            last_file = files[max_file_index]
            last_file_token = files_tokenizer.get_token(last_file)
            last_file_weight = 1 - (max_file_index * file_weight)
            file_token_to_weight[last_file_token] = last_file_weight
            
            
            for file_token in file_token_to_weight.keys():
                file_weight = file_token_to_weight[file_token]
                result[requirement_token][file_token] = file_weight

        return result
