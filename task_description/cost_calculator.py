import numpy as np
from timer import Timer

class CostCalculator:
    def __init__(self, T, deps, C, E, A):
        self.T = T
        self.deps = deps
        self.C = C
        self.E = E
        self.A = A

    def calculate(self):
        T = self.T
        C = self.C
        E = self.E
        A = self.A

        m = np.shape(A)[0]

        f_in = lambda x: 0 if x == 0 else 1
        f_im = lambda x: 0 if x < 1 else 1
    
        result = 0
        for requirements in E:
            
            files = np.dot(requirements, T)
            files_with_dependencies = np.dot(files, self.deps)
            
            plugins = np.dot(files_with_dependencies, A)
            plugins = np.array([f_in(x) for x in plugins])
            
            files_in_delivery = np.dot(A, plugins)
            
            requirements_in_delivery = np.dot(T, files_in_delivery)
            requirements_in_delivery = np.array([f_im(x) for x in requirements_in_delivery])
            
            prices = np.dot(C, requirements_in_delivery)
            
            cost = np.dot(requirements_in_delivery, prices)
            
            result += cost
        return result