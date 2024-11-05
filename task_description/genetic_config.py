# Конфигурация для работы генетического алгоритма
# Настройка осуществляется через редактирование свойств экземпляра класса

class GeneticConfig:
    def __init__(self, space_config):
        self.num_generations = 100
        self.sol_per_pop = 4
        self.num_parents_mating = 2
        self.parent_selection_type = "sss" # sss, rws, sus, rank, random, tournament
        self.keep_parents = 1
        self.crossover_type = "scattered" # single_point, two_points, uniform, scattered
        self.mutation_type = "scramble" # random - не использовать, swap, inversion, scramble, adaptive
        self.mutation_percent_genes = 10
        self.min_value = space_config.min_value
        self.max_value = space_config.max_value
        self.num_genes = space_config.num_genes