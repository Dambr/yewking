# Конфигурация для работы rl с бинарными данными

from gymnasium.spaces import Box, MultiBinary

class RlMultiBinaryConfig:
    def __init__(self, m, k, dtype):
        self.m = m
        self.k = k
        self.dtype = dtype
        
        self.count = m * k
        self.action_space = MultiBinary(self.count)
        self.observation_space = Box(low=0, high=1, shape=(self.count, ), dtype=dtype)