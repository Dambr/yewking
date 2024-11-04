# Реализация rl окружения

import gymnasium as gym
import numpy as np

class RlEnv(gym.Env):
    def __init__(self, config, fitness_calculator, progress, graphic):
        super(RlEnv, self).__init__()
        self.fitness_calculator = fitness_calculator
        self.progress = progress
        self.graphic = graphic
        self.dtype = config.dtype
        self.action_space = config.action_space
        self.observation_space = config.observation_space
        self.default_observation = np.zeros(config.count, dtype=self.dtype)
        self.observation = self.default_observation
        self.best_solution = self.default_observation
        self.best_fitness = 0
        self.info = {}

    def step(self, action):
        self.observation = np.array(action).astype(self.dtype)

        fitness = self.fitness_calculator.calculate(self.observation)
        if fitness >= self.best_fitness:
            self.best_fitness = fitness
            self.best_solution = self.observation
            
        self.graphic.append_value(fitness)

        truncated = False
        terminated = False

        self.progress.value += 1
        return self.observation, float(fitness), terminated, truncated, self.info
    
    def reset(self, seed=None, options=None):
        self.observation = self.default_observation
        self.best_solution = self.default_observation
        self.best_fitness = 0
        return (self.observation, self.info)