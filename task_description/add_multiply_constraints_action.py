# Дополняет модель переменными и ограничениями исключая из нее нелинейность,
# возникающую при умножении двух бинарных переменных

class AddMultiplyConstraintsAction():
    def __init__(self, constraints, varlist):
        self.constraints = constraints
        self.varlist = varlist

    def add_multiply_constraints(self, x, y):
        constraints = self.constraints
        varlist = self.varlist
        
        f = varlist.add()
        constraints.add((x + y <= f + 1))
        constraints.add((f <= x))
        constraints.add((f <= y))
        return f