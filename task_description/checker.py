# Дополняет модель соответствующими ограничениями и переменными в зависимости от того, какие функции проверки были проинициализированы: включения или реализации

import numpy as np


class Checker():
    def __init__(self, constraints, varlist):
        self.constraints = constraints
        self.varlist = varlist

    def check(self, vector, check_function_1, check_function_2):
        constraints = self.constraints
        varlist = self.varlist
        
        result = []
        for x in vector:
            f = varlist.add()
            result.append(f)
            constraint_1 = check_function_1(x, f)
            constraint_2 = check_function_2(x, f)
            constraints.add(constraint_1)
            constraints.add(constraint_2)
            constraints.pprint()
            print()
        return np.array(result)