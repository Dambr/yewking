import numpy as np

class MultiDiscreteConverter:
    def __init__(self, m, k):
        self.m = m
        self.k = k
    
    def convert(self, array):
        A = np.zeros((self.m, self.k))
        for i in range(self.m):
            active_gen = array[i]
            A[i][active_gen] = 1
        return A