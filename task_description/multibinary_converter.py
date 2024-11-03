class MultiBinaryConverter:
    def __init__(self, m, k):
        self.m = m
        self.k = k

    def convert(self, array):
        A = array.reshape(self.m, self.k)
        return A