# Решатель, генерирующий случайное валидное решение
import numpy as np
from random import randint

from timer import Timer

class RandomSolver:
    def __init__(self, m, k, fitness_calculator):
        self.m = m
        self.k = k
        self.fitness_calculator = fitness_calculator

    def solve(self):
        timer = Timer()
        timer.start()
        solution = self.generate_random_solution()
        timer.stop()
        duration = timer.get_duration()

        fitness = self.fitness_calculator.calculate(solution)
        return solution, fitness, duration

    def generate_random_solution(self):
        m = self.m
        k = self.k

        result = [randint(1, k) - 1 for i in range(m)]
        return np.array(result)
