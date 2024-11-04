# Конфигурация для работы rl с дискретными данными

from gymnasium.spaces import Box, MultiDiscrete

class RlMultiDiscreteConfig:
    def __init__(self, m, k, dtype):
        self.m = m
        self.k = k
        self.dtype = dtype

        self.count = m
        self.action_space = MultiDiscrete([k for i in range(m)])
        self.observation_space = Box(low=0, high=k, shape=(m, ), dtype=self.dtype)