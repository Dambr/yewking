# Решение задачи оптимизации заданным решателем

import pyomo.environ as pyo

from solve_result import SolveResult
from timer import Timer

class SolveAction():
    def __init__(self, model, solver_name):
        self.model = model
        self.solver_name = solver_name

    def solve(self):
        solver_name = self.solver_name
        model = self.model
        
        solver = pyo.SolverFactory(solver_name)
        instance = model.create_instance()
        timer = Timer()
        timer.start()
        result = solver.solve(instance)
        timer.stop()
        duration = timer.get_duration()

        result = SolveResult(instance, duration)
        return result