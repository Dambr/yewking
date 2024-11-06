# Решатель на основе rl

from timer import Timer

class RlSolver:
    def __init__(self, model, total_timesteps):
        self.model = model
        self.total_timesteps = total_timesteps

    def solve(self):
        
        timer = Timer()
        timer.start()
        self.model.learn(total_timesteps=self.total_timesteps)
        timer.stop()
        duration = timer.get_duration()
        best_solution = self.model.env.envs[0].env.best_solution
        best_fitness = self.model.env.envs[0].env.best_fitness
        return best_fitness, best_solution, duration

    def plot(self):
        self.model.env.envs[0].env.graphic.plot()