import numpy as np

class PyomoValuesConverter:
    def __init__(self):
        pass

    def convert(self, solution):
        values = solution.extract_values()
        (m, k) = np.shape(solution)
        result = np.zeros((m, k))
        for i in range(m):
            for j in range(k):
                result[i][j] = round(values[(i, j)])
        return result