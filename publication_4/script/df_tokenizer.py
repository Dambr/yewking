class DfTokenizer():

    def __init__(self, df, value_column):
        self.df = df
        self.value_column = value_column

    def get_token(self, value):
        df = self.df
        value_column = self.value_column

        tmp = df[df[value_column] == value]
        index = tmp.index
        values = index.values
        count = len(values)
        if count == 1:
            return values[0]

        raise ValueError("undefined value for " + value)
