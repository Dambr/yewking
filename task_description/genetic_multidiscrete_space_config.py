# Конфигурация для работы генетического алгоритма с дискретными данными

class GeneticMultiDiscreteSpaceConfig:
    def __init__(self, m, k):
        self.min_value = 0
        self.max_value = k - 1

        self.num_genes = m