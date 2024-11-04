# Конфигурация для работы генетического алгоритма с бинарными данными

class GeneticMultiBinarySpaceConfig:
    def __init__(self, m, k):
        self.min_value = 0
        self.max_value = 1

        self.num_genes = m * k