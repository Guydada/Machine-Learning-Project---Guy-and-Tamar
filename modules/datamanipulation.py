from sklearn.impute import SimpleImputer
import numpy as np

class Data:

    def __init__(self, df):
        self.df = df
        pass

    def impute_data(self, df):
        imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
        for feature in df.columns:
            imp.fit(df[feature].values.reshape(-1,1))
            df[feature] = imp.transform(df[feature].values.reshape(-1,1))
        return df