# Построение модели при заданных исходных данных

import numpy as np
import pyomo.environ as pyo

from add_multiply_constraints_action import AddMultiplyConstraintsAction
from calculate_delivery_files_action import CalculateDeliveryFilesAction
from calculate_delivery_requirements_action import CalculateDeliveryRequirementsAction
from calculate_equipment_cost_action import CalculateEquipmentCostAction
from calculate_plugins_action import CalculatePluginsAction
from calculate_useful_files_action import CalculateUsefulFilesAction
from checker import Checker
from implement_checker import ImplementChecker
from include_checker import IncludeChecker


class ModelBuilder():
    # М                                   - условно большое число
    # k                                   - число плагинов
    # T (traceability)        (n x m)     - матрица трассируемости требований к ПО на файлы исходного кода
    # D (dependency)          (m x m)     - матрица зависимостей между файлами исходного кода
    # C (cost)                (n x n)     - матрица расчета стоимости сопровождения требований в поставке
    # E (equirements)         (e x n)     - матрица потребных комплектаций
    def __init__(self, M, k, T, sum_D, C, E):
        self.M = M
        self.k = k
        self.T = T
        self.sum_D = sum_D
        self.C = C
        self.E = E
    
    def build(self):
        M = self.M
        k = self.k
        
        T = self.T
        sum_D = self.sum_D
        C = self.C
        E = self.E

        n, m = np.shape(T)
        
        model = pyo.ConcreteModel(name = 'Optimal decomposition')
        model.constraints = pyo.ConstraintList()
        model.f = pyo.VarList(domain=pyo.Binary)
        model.M = pyo.Param(initialize=M)
        set_n = pyo.Set(initialize=range(n))
        set_n_2 = pyo.Set(initialize = range(2 ** n))
        set_m = pyo.Set(initialize=range(m))
        set_k = pyo.Set(initialize=range(k))
        # A (allocation)          (m x k)     - матрица распределения файлов исходного кода по плагинам
        model.A = pyo.Var(set_m, set_k, domain=pyo.Binary)
        A = np.array(model.A)

        for row in A:
            model.constraints.add((sum(row) == 1))

        equipment_costs = []
        for useful_requirements in E:
            calculate_useful_files_action = CalculateUsefulFilesAction(useful_requirements, T, sum_D)
            checker = Checker(model.constraints, model.f)
            include_checker = IncludeChecker(checker, model.M)
            calculate_plugins_action = CalculatePluginsAction(calculate_useful_files_action, include_checker, A)
            add_multiply_constraints_action = AddMultiplyConstraintsAction(model.constraints, model.f)
            calculate_delivery_files_action = CalculateDeliveryFilesAction(calculate_plugins_action, add_multiply_constraints_action, A)
            implement_checker = ImplementChecker(checker, model.M)
            calculate_delivery_requirements_action = CalculateDeliveryRequirementsAction(calculate_delivery_files_action, implement_checker, T)
            calculate_equipment_cost_action = CalculateEquipmentCostAction(calculate_delivery_requirements_action, add_multiply_constraints_action, C)
            
            equipment_cost = calculate_equipment_cost_action.calculate()
            equipment_costs.append(equipment_cost)
            
        model.OBJ = pyo.Objective(expr = sum(equipment_costs), sense=pyo.minimize)
        return model