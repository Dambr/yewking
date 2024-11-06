# Результат решения задачи оптимизации

import numpy as np

class SolveResult():
    def __init__(self, instance, duration):
        self.instance = instance
        self.duration = duration

    def to_mtx_with_values(self, A):
        values = A.extract_values()
        (m, k) = np.shape(A)
        result = np.zeros((m, k))
        for i in range(m):
            for j in range(k):
                result[i][j] = round(values[(i, j)])
        return result