# Решатель на основе генетического алгоритма

import pygad

from timer import Timer

class GeneticSolver:
    def __init__(self, config, space_config, fitness_calculator, progress):
        self.config = config
        self.space_config = space_config
        self.fitness_calculator = fitness_calculator
        self.progress = progress

    def solve(self):
        
        self.ga_instance = pygad.GA(
                       num_genes=self.space_config.num_genes,
                       init_range_low=self.space_config.min_value,
                       init_range_high=self.space_config.max_value + 1,
                       random_mutation_min_val=self.space_config.min_value,
                       random_mutation_max_val=self.space_config.max_value,
            
                       num_generations=self.config.num_generations,
                       num_parents_mating=self.config.num_parents_mating,
                       sol_per_pop=self.config.sol_per_pop,
                       parent_selection_type=self.config.parent_selection_type,
                       keep_parents=self.config.keep_parents,
                       crossover_type=self.config.crossover_type,
                       mutation_type=self.config.mutation_type,
                       mutation_percent_genes=self.config.mutation_percent_genes,
                       fitness_func=self.fitness_func,
                       on_start=self.on_start,
                       on_fitness=self.on_fitness,
                       on_parents=self.on_parents,
                       on_crossover=self.on_crossover,
                       on_mutation=self.on_mutation,
                       on_generation=self.on_generation,
                       on_stop=self.on_stop,
                       gene_type=int
        )
        
        timer = Timer()
        timer.start()
        self.ga_instance.run()
        timer.stop()
        duration = timer.get_duration()
        best_solution, best_fitness, best_idx, = self.ga_instance.best_solution()
        return best_solution, best_fitness, best_idx, duration

    def on_start(self, ga_instance):
        pass

    def on_fitness(self, ga_instance, fitnesses):
        pass

    def on_parents(self, ga_instance, parents):
        pass

    def on_crossover(self, ga_instance, offspring):
        pass

    def on_mutation(self, ga_instance, offspring):
        pass

    def on_generation(self, ga_instance):
        self.progress.value += 1

    def on_stop(self, ga_instance, fitnesses):
        pass

    def fitness_func(self, ga_instance, solution, solution_idx):
        fitness = self.fitness_calculator.calculate(solution)
        return fitness

    def plot_fitness(self):
        self.ga_instance.plot_fitness()