# Дополняет модель соответствующими ограничениями и переменными для случая реализации

class ImplementChecker():
    def __init__(self, checker, M):
        self.checker = checker
        self.M = M

    def check(self, vector):
        checker = self.checker
        M = self.M

        check_implemented_1 = lambda x, f: (x >= f)
        check_implemented_2 = lambda x, f: (x + 1 / M <= 1 + M * f)

        print('call from implement')
        result = checker.check(vector, check_implemented_1, check_implemented_2)
        return result