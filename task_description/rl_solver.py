# Решатель на основе rl

class RlSolver:
    def __init__(self, model, progress):
        self.model = model
        self.progress = progress

    def solve(self):
        
        self.model.learn(total_timesteps=self.progress.max)
        best_solution = self.model.env.envs[0].env.best_solution
        best_fitness = self.model.env.envs[0].env.best_fitness
        return best_fitness, best_solution

    def plot(self):
        self.model.env.envs[0].env.graphic.show()