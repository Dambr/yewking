import numpy as np

class DependenciesCalculator:
    def __init__(self, D, m, progress):
        self.D = D
        self.m = m
        self.progress = progress

    def calculate(self):
        D = self.D
        m = self.m

        shape = np.shape(D)
        deps = np.zeros(shape)
        deps = self.normalize_deps(deps)
        for j in range(m):
            dep = np.linalg.matrix_power(D, j)
            dep = self.normalize_deps(dep)
            deps += dep
            self.progress.value += 1
        deps = self.normalize_deps(deps)
        return deps

    def normalize_deps(self, deps):
        f_in = lambda x: 0 if x == 0 else 1
        result = [[f_in(el) for el in row] for row in deps]
        return np.array(result)