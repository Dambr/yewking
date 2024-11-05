# Таблица диапазонов значений параметров для групп

import pandas as pd
from random import randint

class VarTable:
    def __init__(self):
        self.K_min = 'K_min'
        self.K_max = 'K_max'
        self.L_min = 'L_min'
        self.L_max = 'L_max'
        self.M_min = 'M_min'
        self.M_max = 'M_max'
        self.N_min = 'N_min'
        self.N_max = 'N_max'
        columns  = [self.K_min, self.K_max, self.L_min, self.L_max, self.M_min, self.M_max, self.N_min, self.N_max]
        data = {
            'G0' : [    2,     2,     1,     1,     2,    10,     2,    10],
            'G1' : [    2,     2,     1,     2,    10,   100,    10,    20],
            'G2' : [    2,     3,     1,     3,   100,   300,    20,    30],
            # 'G3' : [    2,     4,     1,     4,   300,   500,    30,    50],
            # 'G4' : [    3,     5,     2,     5,   500,   800,    50,    80],
            # 'G5' : [    3,     6,     3,     6,   800,  1000,    80,   100],
            # 'G6' : [    4,     7,     4,     7,  1000,  3000,   100,   300],
            # 'G7' : [    5,     8,     5,     8,  3000,  5000,   300,   500],
            # 'G8' : [    6,     9,     6,     9,  5000,  8000,   500,   800],
            # 'G9' : [    7,    10,     7,    10,  8000, 10000,   800,  1000]
        }
        self.df = pd.DataFrame.from_dict(data, orient='index', columns=columns)

    def get_nested_directory(self, group_name, experiment_number):
        nested_directory = 'groups/{}/{}'.format(group_name, experiment_number)
        return nested_directory
    
    def get_group_names(self):
        return self.df.index

    def generate_k(self, group_name):
        k_min = self.df[self.K_min][group_name]
        k_max = self.df[self.K_max][group_name]
        result = randint(k_min, k_max)
        return result

    def generate_l(self, group_name):
        l_min = self.df[self.L_min][group_name]
        l_max = self.df[self.L_max][group_name]
        result = randint(l_min, l_max)
        return result

    def generate_m(self, group_name):
        m_min = self.df[self.M_min][group_name]
        m_max = self.df[self.M_max][group_name]
        result = randint(m_min, m_max)
        return result

    def generate_n(self, group_name):
        n_min = self.df[self.N_min][group_name]
        n_max = self.df[self.N_max][group_name]
        result = randint(n_min, n_max)
        return result