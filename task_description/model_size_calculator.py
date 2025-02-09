class ModelSizeCalculator:
    def __init__(self, k, l, m, n):
        self.k = k
        self.l = l
        self.m = m
        self.n = n

    def calculate_variables_count(self):
        k = self.k
        l = self.l
        m = self.m
        n = self.n

        return m * k + l * (k * (1 + m) + 2 * n)

    def calculate_constraints_count(self):
        k = self.k
        l = self.l
        m = self.m
        n = self.n

        return m + l * (3 * m * k + 2 * k + 5 * n)