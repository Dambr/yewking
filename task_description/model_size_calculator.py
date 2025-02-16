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

        return int(m * k + l * k + l * m * k + l * n + l * n * (n + 1) / 2)

    def calculate_constraints_count(self):
        k = self.k
        l = self.l
        m = self.m
        n = self.n

        return int(m + 2 * l * k + 3 * l * m * k + 2 * l * n + 3 * l * n * (n + 1) / 2)