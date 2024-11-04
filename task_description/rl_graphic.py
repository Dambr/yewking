# Хранитель данных с возможностью их графического отображения

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class RlGraphic:
    def __init__(self, name):
        self.name = name
        self.values = []

    def append_value(self, value):
        self.values.append(value)

    def show(self):
        dataset = {'': self.values}

        df = pd.DataFrame(dataset)
        df_melted = pd.melt(df)
        title = '{}'.format(self.name)
        sns.violinplot(x='variable', y='value', data=df_melted, width=0.5, dodge=False, hue='variable').set(title=title)
        plt.xlabel('')
        plt.ylabel('fitness')