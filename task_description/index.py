from generator_d import GeneratorD
from generator_e import GeneratorE
from generator_p import GeneratorP
from generator_t import GeneratorT
from model_builder import ModelBuilder
from solve_action import SolveAction


M = 10 ** 6

# min values:
# e - 1
# n - 5
# m - 4
# k - 3

# max values:
# e - 10
# n - 25
# m - 15
# k - 10

e = 1
n = 5
m = 4
k = 3

generator_t = GeneratorT(n, m, 1, 2)
generator_d = GeneratorD(m, 0, 1)
generator_p = GeneratorP(n, -5, 10)
generator_e = GeneratorE(e, n, 1, 3)

T = generator_t.generate()
D = generator_d.generate()
P = generator_p.generate()
E = generator_e.generate()

model_builder = ModelBuilder(M, k, T, D, P, E)
model = model_builder.build()

var_count = len(model.A) + len(model.f)
print('var_count', var_count)

solver = SolveAction(model, 'mpec_minlp')
duration = solver.solve().duration
print('duration', duration)