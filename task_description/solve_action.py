# Решение задачи оптимизации заданным решателем

import time
import pyomo.environ as pyo

from solve_result import SolveResult


class SolveAction():
    def __init__(self, model, solver_name):
        self.model = model
        self.solver_name = solver_name

    def solve(self):
        solver_name = self.solver_name
        model = self.model
        
        start_time = time.time()
        solver = pyo.SolverFactory(solver_name)
        instance = model.create_instance()
        result = solver.solve(instance)
        end_time = time.time()
        duration = end_time - start_time

        result = SolveResult(instance, duration)
        return result