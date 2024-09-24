# Дополняет модель соответствующими ограничениями и переменными для случая включения

class IncludeChecker():
    def __init__(self, checker, M):
        self.checker = checker
        self.M = M

    def check(self, vector):
        checker = self.checker
        M = self.M
        
        check_include_1 = lambda x, f: (f + 1 / M <= x + 1)
        check_include_2 = lambda x, f: (x <= M * f)

        print('call from include')
        result = checker.check(vector, check_include_1, check_include_2)
        return result