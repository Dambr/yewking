# Конфигурация для работы генетического алгоритма
# Настройка осуществляется через редактирование свойств экземпляра класса

class GeneticConfig:
    def __init__(self):
        self.num_generations = 100
        self.sol_per_pop = 4
        self.num_parents_mating = 2
        self.parent_selection_type = "sss" # sss, rws, sus, rank, random, tournament
        self.keep_parents = 1
        self.crossover_type = "single_point" # single_point, two_points, uniform, scattered
        self.mutation_type = "swap" # random - не использовать, swap, inversion, scramble, adaptive
        self.mutation_percent_genes = 10

    def to_dict(self):
        result = {
            'num_generations': self.num_generations,
            'sol_per_pop': self.sol_per_pop,
            'num_parents_mating': self.num_parents_mating,
            'parent_selection_type': self.parent_selection_type,
            'keep_parents': self.keep_parents,
            'crossover_type': self.crossover_type,
            'mutation_type': self.mutation_type,
            'mutation_percent_genes': self.mutation_percent_genes
        }
        return result

